def daftar_kandidat(kandidat_set, nama):
    nama = nama.strip().capitalize()

    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_asli = nama_pemilih.strip()
    nama_pemilih = nama_pemilih_asli.lower()
    pilihan = pilihan.strip().capitalize()

    if nama_pemilih in rekap_suara:
        print(f"'{nama_pemilih_asli}' sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print(f"Kandidat '{pilihan}' tidak ditemukan!")
        return

    rekap_suara[nama_pemilih] = pilihan

    print(
        f"Suara '{nama_pemilih_asli}' untuk "
        f"'{pilihan}' berhasil dicatat!"
    )


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1

    return perolehan


def tampilkan_hasil(perolehan):
    print()
    print("========================================")
    print("  HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    for kandidat, jumlah in perolehan.items():
        print(f"  {kandidat}: {jumlah} suara")

    total_suara = sum(perolehan.values())

    print()
    print(f"Total suara masuk: {total_suara}")

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
        return

    suara_tertinggi = max(perolehan.values())

    pemenang = [
        kandidat
        for kandidat, jumlah in perolehan.items()
        if jumlah == suara_tertinggi
    ]

    if len(pemenang) > 1:
        print(f"Hasil SERI antara: {', '.join(pemenang)}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(
            f"PEMENANG: {pemenang[0]} "
            f"dengan {suara_tertinggi} suara!"
        )

    print("========================================")


kandidat_set = set()
rekap_suara = {}

print("========================================")
print("  SISTEM PEMILIHAN KETUA KELAS")
print("========================================")

print()
print("--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama.strip() == "":
        break

    daftar_kandidat(kandidat_set, nama)


if len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat!")

else:
    print()
    print(f"Kandidat terdaftar: {kandidat_set}")

    print()
    print("--- FASE PEMUNGUTAN SUARA ---")

    while True:
        nama_pemilih = input(
            "Nama pemilih (kosongkan untuk selesai): "
        )

        if nama_pemilih.strip() == "":
            break

        print(f"Kandidat yang tersedia: {kandidat_set}")

        pilihan = input("Pilih kandidat: ")

        berikan_suara(
            rekap_suara,
            kandidat_set,
            nama_pemilih,
            pilihan
        )

    perolehan = hitung_suara(
        rekap_suara,
        kandidat_set
    )

    tampilkan_hasil(perolehan)