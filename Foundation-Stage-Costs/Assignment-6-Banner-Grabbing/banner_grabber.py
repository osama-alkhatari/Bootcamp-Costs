import socket
import sys

# مجموعة ثابتة غير قابلة للتعديل لمنافذ الويب
HTTP_PORTS = frozenset({80, 443, 8000, 8080, 8443})


def grab_banner(target_ip, port):
    # الاتصال بالمنفذ وجلب البصمة للخدمة
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)

    try:
        if sock.connect_ex((target_ip, port)) != 0:
            return "CLOSED"

        # إرسال طلب HTTP 
        if port in HTTP_PORTS:
            req = f"HEAD / HTTP/1.1\r\nHost: {target_ip}\r\nConnection: close\r\n\r\n"
            sock.sendall(req.encode("utf-8"))

        raw_data = sock.recv(1024)
        text = raw_data.decode("utf-8", errors="ignore").strip()
        if not text:
            return "OPEN (No Banner)"

        lines = text.splitlines()
        banner = lines[0].strip()

        for line in lines[1:]:
            if line.lower().startswith("server:"):
                banner += f" | {line.strip()}"
                break

        return f"OPEN -> {banner}"

    except socket.timeout:
        return "OPEN (Timeout - No Banner)"
    except OSError:
        return "ERROR (Connection Failed)"
    finally:
        sock.close()


def run_grabber(target, ports_str):
    ports = tuple(int(p.strip()) for p in ports_str.split(",") if p.strip().isdigit())
    print(f"\n[*] Service Banner Scan for {target}:")
    for port in ports:
        print(f" - Port {port:<5}: {grab_banner(target, port)}")


def main():
    if len(sys.argv) > 1:
        t = sys.argv[1]
        p = sys.argv[2] if len(sys.argv) > 2 else "21,22,80,8080"
        run_grabber(t, p)
        return

    while True:
        target = input("\nEnter Target IP [127.0.0.1]: ").strip() or "127.0.0.1"
        ports_in = input("Enter Ports [21,22,80,8080]: ").strip() or "21,22,80,8080"
        run_grabber(target, ports_in)

        try:
            again = input("\nCheck another target? (y/n) [n]: ").strip().lower()
        except EOFError:
            break
        if again != "y":
            print("[*] Exiting Banner Grabber.")
            break


if __name__ == "__main__":
    main()
