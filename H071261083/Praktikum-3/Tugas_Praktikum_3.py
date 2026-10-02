while True:
    soal = int(input ("Masukkan nomor soal yang ingin dijawab (1-3): "))
    print("Ketik '0' untuk menyelesaikan soal")
    print()
    if soal > 3 :
        print("Input tidak valid")



    elif soal == 1:
        print("soal 1")
        print()
        print("---Rekapitulasi Transaksi Dins Store---")
        print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")
        print()
        while True:
            try:
                item = int(input("Masukkan jumlah item:  "))
                if item == 0:
                    break
                elif item < 0:
                    print("Jumlah tidak boleh negatif")
                    print()
                    continue
                elif item > 100:
                    print("Maksimal 100 item per transaksi")
                    print()
                    continue
                else:
                    print(f"Transaksi {item} item berhasil")
                    print()
            except:
                print("Input harus berupa angka")
                print()
        print("Toko ditutup. Sesi rekap selesai")
        print()        



    elif soal == 2:
        print("soal 2")
        print()
        print("---Setup Denah Bioskop NontonYuk---")
        while True:
            try:
                baris = int(input("Masukkan jumlah baris:  "))
                if baris <= 0:
                    print("Jumlah baris harus lebih dari 0")
                    print()
                else:
                    break
            except:
                print("Input baris harus berupa angka")
                print()
        while True:
            try:
                kursi = int(input("Masukkan jumlah kursi:  "))
                if kursi <= 0:
                    print("Jumlah kursi harus lebih dari 0")
                    print()
                else:
                    break
            except:
                print("Input kursi harus berupa angka")
                print()
        print()
        print("--- Daftar Kursi Tersedia ---")
        for a in range(1, baris + 1):
            for b in range(1, kursi + 1):
                if b == 13:
                    continue
                if a == 1 and b % 2 == 0:
                    continue
                print(f"Baris {a}, Kursi {b}")



    elif soal == 3:
        print("soal 3")
        print()
        while True:
            try:
                kursi = int(input("Masukkan maksimal kursi bus:  "))
                if kursi <= 0:
                    print("Jumlah baris harus lebih dari 0")
                    print()
                else:
                    break
            except:
                print("Input jumlah kursi harus berupa angka!")
        print()
        print("---Sistem Reservasi PO BUS Dimulai---")
        print()
        total = 0
        sisa = kursi
        while sisa > 0:
            print()
            print(f"Sisa kursi: {sisa}")
            try:
                umur = int(input("Masukkan umur penumpang:  "))
                if umur < 0:
                    print("Umur tidak valid!")
                    continue
                elif 0 <= umur <= 5:
                    harga = 0
                    print(f"Kategori: Balita - Tiket Gratis Rp ({harga})")
                elif 6 <= umur <= 12:
                    harga = 50000
                    print(f"Kategori: Anak - Harga Rp {harga}")
                elif umur > 12:
                    harga = 100000
                    print(f"Kategori: Dewasa - Harga Rp {harga}")
                else:
                    kursi == 0
                    break
                sisa-= 1
                total = total + harga
            except:
                print("Input kursi harus berupa angka!")
                continue
        print() 
        print("---Semua Kursi Terisi---")
        print(f"Total pendapatan perjalanan PO Bus kali ini: Rp{total}")
        print()



    else:
        break