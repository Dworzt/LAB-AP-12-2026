jawaban = input ("Masukkan nomor soal yang ingin dijalankan (1-4): ")

if jawaban == "1":
    kepedasan = int(input("masukkan presentase cabai : "))

    if kepedasan >= 0 and kepedasan <= 10:
        print("Level Ringan")
    elif kepedasan >= 11 and kepedasan <= 40:
        print("Level Sedang")
    elif kepedasan >= 41 and kepedasan <= 70:
        print("Level Pedas")
    elif kepedasan > 70 and kepedasan <= 100:
        print("Level Ekstrem")
    else:
        print("Presentase cabai tidak valid")
if jawaban == "2":
    jarak_pengiriman = int(input("masukkan jarak: "))

    if jarak_pengiriman < 0:
        tarif_dasar = 0
    elif jarak_pengiriman <= 5:
        tarif_dasar = 10000
    elif jarak_pengiriman <= 20:
        tarif_dasar = 20000
    else:
        tarif_dasar = 35000

    layanan_express = input("layanan express (ya/tidak) : ")

    BIAYA_TAMBAHAN = 15000 if layanan_express == "ya" else 0
    total_tarif_pengiriman = tarif_dasar + BIAYA_TAMBAHAN
    print(f"Total tarif pengiriman: Rp {total_tarif_pengiriman}") 
if jawaban == "3": 
    nilai_tes = int(input("masukkan nilai tes: "))

    if nilai_tes > 100:
        print("melebihi batas nilai")
    elif nilai_tes >= 80 and nilai_tes <= 100:
        print("Lolos ke Tahap Wawancara")
    elif nilai_tes < 80 and nilai_tes >= 65:
        pengalaman_kerja = int(input("masukkan pengalaman kerja (tahun) : "))
        if pengalaman_kerja >= 2:
            print("Lolos Bersyarat")
        else:
            print("Tidak Lolos")
    else:
        print("Tidak Lolos")
if jawaban == "4":
    Tujuan = input("masukkan tujuan (Pantai/Pegunungan/Kota) : ")
    waktu = input("masukkan waktu (Pagi/Malam) : ")
    Tipe_Pengunjung = input("masukkan tipe pengunjung (Anak/Dewasa) : ")

    match Tujuan:
        case "Pantai":
            if waktu == "Pagi":
                print("Paket Rekomendasi: Paket A")  
            elif waktu == "Malam" and Tipe_Pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket rekomendasi")
        case "Pegunungan":
            if waktu == "Pagi" and Tipe_Pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket B")
            elif waktu == "Malam" and Tipe_Pengunjung == "Dewasa":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket rekomendasi")
        case "Kota":
            if waktu == "Malam":
                print("Paket Rekomendasi: Paket C")
            else:
                print("Tidak ada paket rekomendasi")
        case _:
            print("Tidak ada paket rekomendasi")









