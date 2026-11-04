import re

def validasi_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{4,11}", username)

username_valid = []

print("=== SISTEM PENYARINGAN USERNAME ===")

while True:
    username = input("Masukkan username (SELESAI untuk berhenti): ")

    if username == "SELESAI":
        break

    if validasi_username(username):
        print("Username tersedia.")
        username_valid.append(username)
    else:
        print("Username tidak valid!")

print("\nDaftar username yang valid:")
for username in username_valid:
    print(username)

print("Jumlah username valid:", len(username_valid))