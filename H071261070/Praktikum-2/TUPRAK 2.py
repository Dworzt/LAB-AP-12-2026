#PERSENTASE CABE
persentase = float(input("Masukkan persentase cabai: "))

if persentase < 0:
    print("Input tidak valid")
elif persentase <= 10:
    print("Level Aman")
elif persentase <= 40:
    print("Level Sedang")
elif persentase <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")

#tarif pengiriman
jarak = float(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ")

if jarak < 5:
    tarif_dasar = 10000
elif jarak <= 20:
    tarif_dasar = 20000
else:
    tarif_dasar = 35000

biaya_express = 15000 if express == "ya" else 0

total_tarif = tarif_dasar + biaya_express

print("Total tarif pengiriman: Rp", total_tarif)


#kelolosan pelamar
nilai = float(input("Masukkan nilai tes: "))
pengalaman = float(input("Masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")

#rekomendasi paket wisata
tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
pengunjung = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and pengunjung == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")
