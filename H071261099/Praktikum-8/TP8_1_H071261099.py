import re

print("=== Validasi Data Mahasiswa ===")

def validasi_nim(nim):
    return re.fullmatch(r"H071\d{6}", nim)

def validasi_email(email):
    return re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email)

def validasi_telepon(telepon):
    return re.fullmatch(r"\d{10,13}", telepon)

nim = input("Masukkan NIM       : ")
email = input("Masukkan Email     : ")
telepon = input("Masukkan No. Telp  : ")

print("\n--- Hasil Validasi ---")

nim_valid = validasi_nim(nim)
email_valid = validasi_email(email)
telepon_valid = validasi_telepon(telepon)

if nim_valid:
    print("NIM        : Valid")
else:
    print("Format NIM tidak valid!")

if email_valid:
    print("Email      : Valid")
else:
    print("Format email tidak valid!")

if telepon_valid:
    print("No. Telepon: Valid")
else:
    print("Nomor telepon tidak valid!")

if nim_valid and email_valid and telepon_valid:
    print("\nData mahasiswa berhasil diverifikasi!")