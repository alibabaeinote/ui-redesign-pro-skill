# UI Redesign Pro (Claude skill)

[فارسی](#فارسی) | [English](#english)

## English

A Claude skill that redesigns or designs UI screens through a fixed, checkable pipeline: locale check, numbered audit of current problems, live benchmark, three structurally different versions, one combined best-of-three version, usability refinement, a measured pixel-perfect pass, and a one-page management report that justifies each decision.

**What it commits to.** Content, topic, purpose, business goal, audience and every function inside the UI stay the same. The original visual style is not carried over unless your brief names it. Components and navigation may be redesigned or replaced by best-practice ones when that improves usability, learnability or navigation.

**Status.** Version 0.10.0. Not yet validated on real projects; see CHANGELOG.

### Install
Copy the `ui-redesign-pro/` folder into your skills directory (for Claude Code: `~/.claude/skills/`). Uploading a zip in the Claude app settings may also work; this has not been tested.

### Use
Give it a screen (image, Figma link, HTML or description) and a short brief. Say if any visual constraint must stay (brand colors, font, icon family). It asks at most one question, then works.

### Contents
- `ui-redesign-pro/SKILL.md`: the skill.
- `ui-redesign-pro/references/`: design systems, typography and color, pattern libraries, trend research, and the pixel-perfect checklist.
- `examples/`: report template (case studies to come).
- `docs/`: pipeline diagram and the evaluation protocol.
- `evaluation/`: kit to test the skill against a plain prompt (blind rating, measured items).
- `scripts/validate.py`: package checks, also run in CI.

### License
MIT. See `LICENSE`.

## فارسی

این اسکیل برای Claude است و طراحی یا بازطراحی صفحه‌های UI را در یک مسیر ثابت و قابل‌بررسی انجام می‌دهد: تشخیص زبان و جهت (Locale Gate)، ممیزی مشکل‌های فعلی با شماره‌ی P1 تا Pn، بنچمارک زنده، سه نسخه‌ی ساختاری متفاوت، ترکیب بهترین‌ها در یک نسخه، پالایش کاربردپذیری، گذر پیکسل‌دقیق با اندازه‌گیری، و در پایان یک سند یک‌صفحه‌ای برای مدیران که دلیل هر تصمیم را می‌گوید.

**تعهد اسکیل.** محتوا، موضوع، هدف صفحه، هدف کسب‌وکار، مخاطب و همه‌ی قابلیت‌های داخل UI ثابت می‌ماند. سبک بصری قبلی نگه داشته نمی‌شود، مگر در بریف نام برده شود. کامپوننت‌ها و ناوبری در صورت بهبود کاربردپذیری یا آموزش‌پذیری می‌توانند بازطراحی یا با بهترین‌روش (best practice) جایگزین شوند.

**وضعیت.** نسخه‌ی 0.10.0. هنوز روی پروژه‌ی واقعی اعتبارسنجی نشده است. جزئیات در CHANGELOG.

### نصب
پوشه‌ی `ui-redesign-pro/` را در پوشه‌ی اسکیل‌ها کپی کنید (برای Claude Code مسیر `~/.claude/skills/`). آپلود zip در تنظیمات اپ Claude هم ممکن است کار کند، ولی امتحان نشده است.

### استفاده
یک صفحه (تصویر، لینک Figma، HTML یا توضیح) و یک بریف کوتاه بدهید. اگر محدودیت بصری دارید (رنگ برند، فونت، خانواده‌ی آیکون) بگویید. اسکیل حداکثر یک سؤال می‌پرسد و بعد کار را انجام می‌دهد.

### محتوا
- `ui-redesign-pro/SKILL.md`: خود اسکیل.
- `ui-redesign-pro/references/`: سیستم‌های طراحی، تایپوگرافی و رنگ، کتابخانه‌ی الگوها، پژوهش ترند و چک‌لیست پیکسل‌دقیق.
- `examples/`: قالب سند مدیران (نمونه‌های واقعی بعداً اضافه می‌شود).
- `docs/`: نمودار مسیر کار و پروتکل ارزیابی.
- `evaluation/`: کیت آزمون اسکیل در برابر پرامپت ساده (امتیازدهی کورکورانه و معیارهای اندازه‌گیری‌شده).
- `scripts/validate.py`: بررسی خودکار بسته، در CI هم اجرا می‌شود.

### مجوز
MIT. فایل `LICENSE` را ببینید.
