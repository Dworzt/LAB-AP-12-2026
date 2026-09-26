jawaban = input ("masukkan nomor soal yang ingin di jalankan (1-3): ")

match jawaban:
    case "1":
        
        print("=== Program Kasir Dins Store (Roblox Fish It) ===")
        print()
        print("ketik '0' untuk menutup toko dan mengakhiri sesi.")
        print()
        while True:
            try:
                user_input = input("Masukkan jumlah item: ")
                jumlah = int(user_input)
            
                if jumlah == 0:
                    print("Toko ditutup. Sesi rekap selesai.")
                    break
                
                elif jumlah < 0:
                    print("Jumlah tidak boleh negatif")
                    continue
                elif jumlah > 100:
                    print("Maksimal 100 item per transaksi!")
                    continue
                else:
                    print(f"Transaksi {jumlah} item berhasil!")
                
            except ValueError:
                print("Input harus berupa angka!")

    case "2":
        print("---Setup Denah Bioskop NontonYuk---")
        print()
        while True:
            try:
                N = int(input("Masukkan jumlah baris: "))

                if N <= 0:
                    print("Jumlah baris harus lebih dari 0!")
                    continue

                break

            except ValueError :
                print("Input baris harus berupa angka!")


        while True:
            try:
                M = int(input("Masukkan jumlah kursi per baris: "))

                if M <= 0:
                    print("Jumlah kursi per baris harus lebih dari 0!")
                    continue

                break

            except ValueError:
                print("Input jumlah kursi per baris harus berupa angka!")


        print("---Daftar Kursi Tersedia---")
        for baris in range(1, N + 1):
            for kursi in range(1, M + 1):

                if kursi == 13:
                    continue

                if baris == 1 and kursi % 2 == 0:
                    continue
                
                print(f"Baris {baris} - Kursi {kursi}")
    case "3":
        while True:
            try:
                N = int(input("Masukkan maksimal kursi bus: "))

                if N <= 0:
                    print("Jumlah kursi harus lebih dari 0!")
                else:
                    break
            except ValueError:
                print("Input jumlah kursi harus berupa angka!")

        sisa_kursi = N
        total_pendapatan = 0

        print("--- Sistem Reservasi PO BUS Dimulai ---")

        while sisa_kursi > 0:
            print("Sisa kursi:", sisa_kursi)

            try:
                umur = int(input("Masukkan umur penumpang: "))
            except ValueError:
                print("Input umur harus berupa angka!")
                continue

            if umur < 0:
                print("Umur tidak valid!")
                continue

            elif umur <= 5:
                kategori = "Balita"
                harga = 0
                print("Kategori: Balita - Tiket Gratis (Rp 0)")
                

            elif umur <= 12:
                kategori = "Anak"
                harga = 50000
                print("Kategori: Anak - Harga: Rp 50.000")

            else:
                kategori = "Dewasa"
                harga = 100000
                print("Kategori: Dewasa - Harga: Rp 100.000")

            sisa_kursi -= 1
            total_pendapatan += harga

        print("--- Semua Kursi Terisi ---")
        print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)