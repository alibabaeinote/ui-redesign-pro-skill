#!/usr/bin/env python3
"""Automated, objective measurements of HTML outputs with headless Chrome (Playwright).

Measures: WCAG contrast failures, interactive target sizes, font sizes, distinct font sizes,
horizontal overflow, interactive count, and content parity against the baseline input.
Usage: measure.py INPUTS_DIR RUNS_DIR OUT_DIR [--chrome /usr/bin/google-chrome]
"""
import argparse, csv, json, re
from pathlib import Path
from playwright.sync_api import sync_playwright

VIEWPORTS = {"s1": (1280, 800), "s2": (1280, 800), "s3": (1280, 800), "s4": (390, 844), "s5": (390, 844)}

JS = r"""
() => {
  const parse = c => { const m = c.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p = m[1].split(',').map(s=>parseFloat(s)); return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1}; };
  const over = (f,b) => ({r:f.r*f.a+b.r*(1-f.a), g:f.g*f.a+b.g*(1-f.a), b:f.b*f.a+b.b*(1-f.a), a:1});
  const lin = v => { v/=255; return v<=0.03928? v/12.92 : Math.pow((v+0.055)/1.055,2.4); };
  const L = c => 0.2126*lin(c.r)+0.7152*lin(c.g)+0.0722*lin(c.b);
  const ratio = (a,b) => { const x=L(a), y=L(b); return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05); };
  const bgOf = el => { let layers=[]; let n=el; let unknown=false;
    while(n && n.nodeType===1){ const cs=getComputedStyle(n); if(cs.backgroundImage && cs.backgroundImage!=='none') unknown=true;
      const c=parse(cs.backgroundColor); if(c && c.a>0){ layers.push(c); if(c.a>=1) break; } n=n.parentElement; }
    let base={r:255,g:255,b:255,a:1}; for(let i=layers.length-1;i>=0;i--) base=over(layers[i],base); return {c:base, unknown}; };
  const visible = el => { const r=el.getBoundingClientRect(); const cs=getComputedStyle(el); return r.width>0 && r.height>0 && cs.visibility!=='hidden' && cs.display!=='none' && parseFloat(cs.opacity)>0; };
  const out = {contrastFail:0, contrastChecked:0, contrastUnknown:0, fails:[], sizes:new Set(), minFont:999, texts:[], inter:0, t24:0, t44:0, small:[]};
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let tn;
  while(tn = walker.nextNode()){
    const s = tn.nodeValue.replace(/\s+/g,' ').trim(); if(!s) continue;
    const el = tn.parentElement; if(!el || !visible(el) || ['SCRIPT','STYLE','TITLE'].includes(el.tagName)) continue;
    out.texts.push(s);
    const cs = getComputedStyle(el); const fs = parseFloat(cs.fontSize); out.sizes.add(fs); out.minFont = Math.min(out.minFont, fs);
    const fg = parse(cs.color); const {c:bg, unknown} = bgOf(el);
    if(unknown){ out.contrastUnknown++; continue; }
    const fgc = over(fg, bg); const r = ratio(fgc,bg);
    const bold = parseInt(cs.fontWeight)>=700; const large = fs>=24 || (fs>=18.66 && bold);
    out.contrastChecked++;
    if(r < (large?3:4.5)){ out.contrastFail++; if(out.fails.length<8) out.fails.push(s.slice(0,30)+' '+r.toFixed(2)); }
  }
  const sel = 'a[href],button,input:not([type=hidden]),select,textarea,[role=button],[role=tab],[role=link],[tabindex]:not([tabindex="-1"]),summary';
  document.querySelectorAll(sel).forEach(el=>{ if(!visible(el)) return; out.inter++;
    const r = el.getBoundingClientRect(); const inl = getComputedStyle(el).display==='inline' && el.tagName==='A';
    if(inl) return; // inline text links are exempt from the 24px floor (WCAG 2.2 inline exception)
    if(r.width<24 || r.height<24){ out.t24++; if(out.small.length<8) out.small.push((el.textContent||el.tagName).trim().slice(0,20)+' '+Math.round(r.width)+'x'+Math.round(r.height)); }
    if(r.width<44 || r.height<44) out.t44++; });
  out.sizes = [...out.sizes].sort((a,b)=>a-b);
  out.overflowX = document.documentElement.scrollWidth > window.innerWidth + 1;
  out.dir = document.documentElement.getAttribute('dir') || 'ltr';
  return out;
}
"""

def norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()

def run(page, path, vp):
    page.set_viewport_size({"width": vp[0], "height": vp[1]})
    page.goto(path.resolve().as_uri()); page.wait_for_timeout(300)
    return page.evaluate(JS)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", type=Path); ap.add_argument("runs", type=Path); ap.add_argument("out", type=Path)
    ap.add_argument("--chrome", default="/usr/bin/google-chrome")
    a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
    rows = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=a.chrome, args=["--no-sandbox"]); page = b.new_page()
        for inp in sorted(a.inputs.glob("s*.html")):
            sid = inp.stem.split("-")[0]; screen = inp.stem; vp = VIEWPORTS[sid]
            base = run(page, inp, vp)
            page.screenshot(path=str(a.out / f"{screen}__orig.png"), full_page=True)
            base_texts = {norm(t) for t in base["texts"]}
            variants = [("orig", inp)] + [(c, a.runs / screen / c / "index.html") for c in ("A", "B")]
            for cond, path in variants:
                if not path.exists():
                    rows.append({"screen": screen, "condition": cond, "status": "MISSING"}); continue
                m = base if cond == "orig" else run(page, path, vp)
                if cond != "orig": page.screenshot(path=str(a.out / f"{screen}__{cond}.png"), full_page=True)
                out_text = " ".join(norm(t) for t in m["texts"])
                missing = sorted(t for t in base_texts if t not in out_text)
                rows.append({"screen": screen, "condition": cond, "status": "ok",
                  "contrast_failures": m["contrastFail"], "contrast_checked": m["contrastChecked"], "contrast_unknown_bg": m["contrastUnknown"],
                  "target_size_violations": m["t24"], "targets_under_44": m["t44"], "interactive_count": m["inter"],
                  "min_font_px": m["minFont"], "distinct_font_sizes": len(m["sizes"]),
                  "content_parity_pct": round(100 * (len(base_texts) - len(missing)) / max(1, len(base_texts)), 1),
                  "missing_strings": " | ".join(missing)[:200], "overflow_x": int(m["overflowX"]), "dir": m["dir"],
                  "worst_contrast": "; ".join(m["fails"][:3]), "small_targets": "; ".join(m["small"][:3])})
        b.close()
    fields = ["screen","condition","status","contrast_failures","contrast_checked","contrast_unknown_bg","target_size_violations","targets_under_44","interactive_count","min_font_px","distinct_font_sizes","content_parity_pct","overflow_x","dir","missing_strings","worst_contrast","small_targets"]
    with open(a.out / "measurements.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore"); w.writeheader(); w.writerows(rows)
    print(json.dumps([{k: r.get(k) for k in ("screen","condition","contrast_failures","target_size_violations","min_font_px","distinct_font_sizes","content_parity_pct","overflow_x")} for r in rows], indent=0)[:3000])

if __name__ == "__main__":
    main()
