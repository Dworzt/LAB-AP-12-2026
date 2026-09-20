soal = input ("Masukkan nomor soal yang ingin dijawab (1-4): ")

if soal == "1":

    persentase = int(input("Masukkan persentase cabai: "))

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

if soal == "2":

    jarak = int(input("Masukkan jarak pengiriman (km): "))
    express = input("Layanan express (ya/tidak): ")

    if jarak < 0:
        print("Input jarak tidak valid")
    elif jarak == 0:
        print("gratis tarif pengiriman")
    elif jarak < 5:
        tarif_dasar = 10000
    elif jarak <= 20:
        tarif_dasar = 20000
    else:
        tarif_dasar = 35000

    if jarak > 0:
        biaya_express = 15000 if express == "ya" else 0
        total_tarif = tarif_dasar + biaya_express
        print(f"Total tarif pengiriman: Rp{total_tarif}")

if soal == "3":

    nilai = int(input("Masukkan nilai tes: "))
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

    if nilai and pengalaman < 0:
        print ("input tidak valid")
    elif nilai >= 80 and pengalaman >= 0:
        print("Lolos ke Tahap Wawancara")
    elif nilai >= 65 and pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")

if soal == "4":

    tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
    waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
    tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()

    match tujuan:
        case "Pantai":
            if waktu == "Pagi":
                paket = "Paket A"
            else:
                if waktu == "Malam" and tipe == "Dewasa":
                    paket = "Paket C"
                else:
                    paket = "Tidak ada paket yang cocok"

        case "Pegunungan":
            if waktu == "Pagi" and tipe == "Dewasa":
                paket = "Paket B"
            else:
                if waktu == "Malam" and tipe == "Dewasa":
                    paket = "Paket C"
                else:
                    paket = "Tidak ada paket yang cocok"

        case "Kota":
            if waktu == "Malam":
                paket = "Paket C"
            else:
                paket = "Tidak ada paket yang cocok"

        case _:
            paket = "Tidak ada paket yang cocok"
            
    print(f"Paket Rekomendasi: {paket}")