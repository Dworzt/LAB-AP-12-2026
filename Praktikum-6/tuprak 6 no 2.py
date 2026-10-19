print("=" * 40)
print("SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

kandidat = set()

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama_kandidat = input(
        "Masukkan nama kandidat (kosongkan untuk selesai): "
    )

    if nama_kandidat == "":
        break

    kandidat.add(nama_kandidat)
    print(
        f"'{nama_kandidat}' berhasil "
        f"didaftarkan sebagai kandidat!"
    )

print(f"\nKandidat terdaftar: {kandidat}")

hasil_suara = {
    nama: 0
    for nama in kandidat
}

pemilih = set()

print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input(
        "\nNama pemilih (kosongkan untuk selesai): "
    )

    if nama_pemilih == "":
        break

    print(f"Kandidat yang tersedia: {kandidat}")

    pilihan = input("Pilih kandidat: ")

    if nama_pemilih in pemilih:
        print(
            f"'{nama_pemilih}' sudah memberikan "
            f"suara sebelumnya!"
        )
        continue

    if pilihan not in kandidat:
        print("Kandidat tidak terdaftar!")
        continue

    hasil_suara[pilihan] += 1
    pemilih.add(nama_pemilih)

    print(
        f"Suara '{nama_pemilih}' untuk "
        f"'{pilihan}' berhasil dicatat!"
    )

print("\n" + "=" * 40)
print("HASIL PEMILIHAN KETUA KELAS")
print("=" * 40)

for nama, suara in hasil_suara.items():
    print(f"{nama}: {suara} suara")

total_suara = sum(hasil_suara.values())

print(f"\nTotal suara masuk: {total_suara}")

if total_suara > 0:
    pemenang = max(
        hasil_suara,
        key=hasil_suara.get
    )

    print(
        f"PEMENANG: {pemenang} "
        f"dengan {hasil_suara[pemenang]} suara!"
    )

print("=" * 40)