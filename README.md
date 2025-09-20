# xss-sqli-python

english:


# ASCII CLI Scanner - SQLi & XSS

A **terminal-based web vulnerability testing tool** for **SQL Injection and XSS** with a block-style ASCII design and multi-threaded scanning. This tool supports **Pause/Resume**, **color-coded terminal output**, and **CSV & timestamped log export**.

---

## Features

* **Block-style ASCII Banner** at startup

* **SQL Injection & XSS scanning** with pre-defined payloads

* **Threaded scanning** for faster performance

* **Pause/Resume with Enter**

* **Color-coded Progress Bar**

* **Color-coded terminal results**:

  * SQLi success → Red
  * XSS success → Yellow
  * Safe → Green
  * Timestamp → Grey

* **CSV output** with all results

* **Timestamped log file** with real-time updates

---

## Requirements

* Python 3.x
* `requests` library

Install `requests`:

```bash
pip install requests
```

---

## Usage

1. Clone or download the project:

```bash
git clone https://github.com/username/ascii-cli-scanner.git
cd ascii-cli-scanner
```

2. Run the tool:

```bash
python3 scanner.py
```

3. Enter the required information:

   * Target URL (e.g., `http://test.com/page`)
   * Parameter to test (e.g., `id`)
   * CSV output filename
   * Log filename

4. During scanning, press **Enter** to **Pause/Resume** the scan.

---

## Terminal Output Example

```
  __  ______ ____       ____   ___  _     _
 \ \/ / ___/ ___|     / ___| / _ \| |   (_)
  \  /\___ \___ \ ____\___ \| | | | |   | |
  /  \ ___) |__) |_____|__) | |_| | |___| |
 /_/\_\____/____/     |____/ \__\_\_____|
                                           
         ASCII CLI Scanner - SQLi & XSS

[2025-09-20 20:00:01] SQLi  | ' OR '1'='1              | VULN
[2025-09-20 20:00:01] XSS   | <script>alert(1)</script> | safe
[##########----------------------] 2/4
```

---

## Output

* **CSV** with columns: `Timestamp | Type | Payload | Detected`
* **Log** plain-text timestamped file including all messages

---

## Notes

* For **personal testing and educational purposes only**.
* Testing on websites without permission is **illegal**.




persian:

# xss-sqli-python

# اسکنر ترمینالی ASCII - SQLi و XSS

یک **ابزار تست آسیب‌پذیری وب در ترمینال** برای **SQL Injection و XSS** با طراحی بلوکی ASCII و قابلیت اسکن چندرشته‌ای. این ابزار از **Pause/Resume**، **نمایش رنگی در ترمینال** و **خروجی CSV و فایل لاگ زمان‌دار** پشتیبانی می‌کند.

---

## ویژگی‌ها

* **بنر بلوکی ASCII** در ابتدای ابزار

* **تست SQL Injection و XSS** با payload های از پیش تعریف شده

* **اسکن چندرشته‌ای** برای سرعت بالاتر

* **Pause/Resume با Enter**

* **Progress Bar رنگی**

* **نتایج رنگی در ترمینال**:

  * موفقیت SQLi → قرمز
  * موفقیت XSS → زرد
  * Safe → سبز
  * Timestamp → خاکستری

* **خروجی CSV** با تمام نتایج

* **فایل لاگ زمان‌دار** با نتایج در لحظه

---

## پیش‌نیازها

* Python 3.x
* کتابخانه `requests`

نصب `requests`:

```bash
pip install requests
```

---

## استفاده

1. Clone یا دانلود پروژه:

```bash
git clone https://github.com/username/ascii-cli-scanner.git
cd ascii-cli-scanner
```

2. اجرای ابزار:

```bash
python3 scanner.py
```

3. وارد کردن اطلاعات مورد نیاز:

   * Target URL (مثال: `http://test.com/page`)
   * پارامتر برای تست (مثال: `id`)
   * نام فایل خروجی CSV
   * نام فایل لاگ

4. هنگام اجرای اسکن، فشار دادن **Enter** برای **Pause/Resume**

---

## نمونه خروجی ترمینال

```
  __  ______ ____       ____   ___  _     _
 \ \/ / ___/ ___|     / ___| / _ \| |   (_)
  \  /\___ \___ \ ____\___ \| | | | |   | |
  /  \ ___) |__) |_____|__) | |_| | |___| |
 /_/\_\____/____/     |____/ \__\_\_____|
                                           
         اسکنر ترمینالی ASCII - SQLi و XSS

[2025-09-20 20:00:01] SQLi  | ' OR '1'='1              | VULN
[2025-09-20 20:00:01] XSS   | <script>alert(1)</script> | safe
[##########----------------------] 2/4
```

---

## خروجی

* **CSV** با ستون‌های: `Timestamp | Type | Payload | Detected`
* **Log** فایل متن ساده زمان‌دار شامل همه پیام‌ها

---

## توجه‌ها

* فقط برای **آزمایش و آموزش شخصی** استفاده شود.
* تست روی وب‌سایت‌های دیگر بدون اجازه **غیرقانونی است**.

---

## License

MIT License



MIT License
