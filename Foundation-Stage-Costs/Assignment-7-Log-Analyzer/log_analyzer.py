import re
import os
import sys
from collections import Counter

# أنماط الهجمات محفوظة في Tuple غير قابل للتعديل (Immutable)
PATTERNS = (
    ("SQL Injection", re.compile(r"(union\s+select|or\s+'1'='1|drop\s+table|sqlmap)", re.IGNORECASE)),
    ("Command Injection", re.compile(r"(;\s*cat|/bin/sh|nikto)", re.IGNORECASE)),
    ("Path Traversal", re.compile(r"(\.\./|\.\.%2f|/etc/passwd|/etc/shadow)", re.IGNORECASE)),
    ("XSS Attack", re.compile(r"(<script|onerror\s*=|alert\s*\()", re.IGNORECASE)),
)

IP_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def analyze_logs(file_path):
    if not os.path.exists(file_path):
        print(f"[!] Error: File not found '{file_path}'")
        return

    summary = Counter()
    ip_counts = Counter()
    total_alerts = 0

    print(f"\n[*] Analyzing Log File: {os.path.basename(file_path)}\n")

    # قراءة ملف السجلات سطراً بسطر
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line_num, line in enumerate(f, start=1):
            ip_match = IP_REGEX.search(line)
            ip = ip_match.group(0) if ip_match else "Unknown"

            for attack_type, pattern in PATTERNS:
                if re.search(pattern, line):
                    total_alerts += 1
                    summary[attack_type] += 1
                    ip_counts[ip] += 1
                    print(f"[ALERT] Line {line_num:<2} | Type: {attack_type:<18} | Attacker IP: {ip}")
                    break

    # ملخص إجمالي للهجمات المكتشفة وأنواعها
    print(f"\n[*] Scan Summary (Total Alerts: {total_alerts}):")
    for atk, count in summary.items():
        print(f" - {atk:<18}: {count}")

    if ip_counts:
        top_ip, hits = ip_counts.most_common(1)[0]
        print(f"[*] Top Attacking IP  : {top_ip} ({hits} attempts)")


def main():
    default_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "access.log")

    if len(sys.argv) > 1:
        analyze_logs(sys.argv[1])
        return

    #حلقة تكرار لتحليل من جديد 
    while True:
        user_file = input(f"\nEnter Log File Path [access.log]: ").strip()
        target_path = user_file if user_file else default_file
        analyze_logs(target_path)

        try:
            again = input("\nAnalyze another log file? (y/n) [n]: ").strip().lower()
        except EOFError:
            break
        if again != "y":
            print("[*] Exiting Log Analyzer.")
            break


if __name__ == "__main__":
    main()
