import re

print("=== Pembersihan Data Nomor Telepon ===")

jumlah = int(input("Masukkan jumlah data: "))

data_telepon = []

for i in range(jumlah):
    nomor = input(f"\nNomor ke-{i+1}: ")
    data_telepon.append(nomor)

print("\n--- Hasil Pembersihan ---")

jumlah_valid = 0

for i, nomor in enumerate(data_telepon):
    bersih = re.sub(r"[\s-]", "", nomor)

    if re.fullmatch(r"\d{10,13}", bersih):
        status = "Valid"
        jumlah_valid += 1
    else:
        status = "Tidak valid"

    print(f"\nData {i+1}:")
    print("Sebelum :", nomor)
    print("Sesudah :", bersih)
    print("Status  :", status)

print("\nJumlah nomor valid:", jumlah_valid)