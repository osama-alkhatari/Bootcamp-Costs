import hashlib
import os
import stat
import sys
import time
from datetime import datetime

CHUNK_SIZE = 4096


def get_file_hash(file_path):
    # قراءة الملف بنمط ثنائي (rb) على أجزاء (chunks) وحساب SHA-256
    if not os.path.exists(file_path):
        return None

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            sha256.update(chunk)
    return sha256.hexdigest()


def lock_baseline_file(baseline_hash, target_name):
    # حفظ البصمة المرجعية وقفل الملف بصلاحية قراءة فقط (Read-Only) لمنع التعديل
    b_file = "baseline.sha256"
    if os.path.exists(b_file):
        os.chmod(b_file, stat.S_IWRITE | stat.S_IREAD)
    with open(b_file, "w", encoding="utf-8") as f:
        f.write(f"{baseline_hash}  {target_name}\n")
    os.chmod(b_file, stat.S_IREAD)


def log_alert(msg):
    now = datetime.now().strftime("%H:%M:%S")
    line = f"[{now}] {msg}"
    print(line)
    with open("fim_alerts.log", "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")


def monitor_file(file_path, interval=3):
    baseline_hash = get_file_hash(file_path)
    if not baseline_hash:
        print(f"[!] Error: Target file not found '{file_path}'")
        return

    lock_baseline_file(baseline_hash, os.path.basename(file_path))

    print(f"[*] Monitoring File  : {os.path.basename(file_path)}")
    print(f"[*] Baseline SHA-256 : {baseline_hash} (Locked Read-Only)\n")

    try:
        # حلقة تكرارية مستمرة لفحص سلامة الملف كل 3 ثوانٍ
        while True:
            time.sleep(interval)
            current_hash = get_file_hash(file_path)

            if current_hash is None:
                log_alert("[CRITICAL ALERT] Target file was deleted or moved!")
            elif current_hash != baseline_hash:
                log_alert(f"[CRITICAL ALERT] Unauthorized modification detected! New Hash: {current_hash[:16]}...")
            else:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] [OK] File integrity verified (Matches Baseline).")
    except KeyboardInterrupt:
        print("\n[*] FIM Monitoring stopped by user.")


if __name__ == "__main__":
    default_target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sensitive_config.conf")
    target = sys.argv[1] if len(sys.argv) > 1 else default_target
    monitor_file(target)
