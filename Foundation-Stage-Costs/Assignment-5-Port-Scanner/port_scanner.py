import socket
import time
import sys
from concurrent.futures import ThreadPoolExecutor

# قائمة المنافذ المشهوره 
SERVICES = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPC",
    139: "NetBIOS", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 8080: "HTTP-Alt"
}


def scan_port(target_ip, port):
    # فحص منفذ واحد مع ضبط وقت وا مهلة الاتصال
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        if sock.connect_ex((target_ip, port)) == 0:
            service = SERVICES.get(port, "Unknown")
            print(f"[+] Port {port:<5} : OPEN  ({service})")
            return port, service
    except OSError:
        pass
    finally:
        sock.close()
    return None


def run_scan(target, start_p=1, end_p=1024):
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: Invalid target '{target}'")
        return

    ports = tuple(range(start_p, end_p + 1))
    print(f"\n[*] Scanning {target_ip} (Ports: {start_p}-{end_p})...")
    start_time = time.time()

    # فحص متساوي  باستخدام 50 خيطاً
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target_ip, p), ports)
        open_ports = tuple(r for r in results if r is not None)

    elapsed = time.time() - start_time
    print(f"[*] Scan finished in {elapsed:.2f}s | Open ports found: {len(open_ports)}")

    with open("scan_results.txt", "w", encoding="utf-8") as f:
        f.write(f"Target: {target_ip} ({start_p}-{end_p}) | Time: {elapsed:.2f}s\n")
        for p, srv in open_ports:
            f.write(f"Port {p:<5}: OPEN ({srv})\n")


def main():
    if len(sys.argv) > 1:
        t = sys.argv[1]
        sp = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        ep = int(sys.argv[3]) if len(sys.argv) > 3 else 1024
        run_scan(t, sp, ep)
        return

    # شرط لاعداة العملية
    while True:
        target = input("\nEnter Target IP [127.0.0.1]: ").strip() or "127.0.0.1"
        s_in = input("Start Port [1]: ").strip()
        e_in = input("End Port [1024]: ").strip()

        start_p = int(s_in) if s_in.isdigit() else 1
        end_p = int(e_in) if e_in.isdigit() else 1024
        run_scan(target, start_p, end_p)

        try:
            again = input("\nScan another target? (y/n) [n]: ").strip().lower()
        except EOFError:
            break
        if again != "y":
            print("[*] Exiting Port Scanner.")
            break


if __name__ == "__main__":
    main()
