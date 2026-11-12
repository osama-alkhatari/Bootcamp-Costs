import secrets
import string
import hashlib
import sys


CHAR_POOL = string.ascii_letters + string.digits + string.punctuation


def generate_password(length=16):
    if length < 8:
        length = 8

    # ضمان وجود محرف واحد على الأقل من كل فئة ثم اكمال او انتهاء الطول المطلوب
    pwd = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation),
    ]
    pwd += [secrets.choice(CHAR_POOL) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(pwd)
    return "".join(pwd)


def calculate_sha256(text):
    # ترميز النص وحساب قيمة التجزئة بصيغة Hexadecimal
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def show_result(text):
    sha256_hex = calculate_sha256(text)
    salt = secrets.token_hex(8)
    salted_hex = calculate_sha256(salt + text)

    print(f"\n[+] Generated Password ({len(text)} chars) : {text}")
    print(f"[+] SHA-256 Hash (Hex)           : {sha256_hex}")
    print(f"[*] Salted SHA-256 (Salt={salt}): {salted_hex}")


def main():
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        show_result(generate_password(int(sys.argv[1])))
        return

    while True:
        user_in = input("\nEnter desired password length [16]: ").strip()
        length = int(user_in) if user_in.isdigit() else 16
        show_result(generate_password(length))

        try:
            again = input("\nGenerate another password? (y/n) [n]: ").strip().lower()
        except EOFError:
            break
        if again != "y":
            print("[*] Exiting Password Generator.")
            break


if __name__ == "__main__":
    main()
