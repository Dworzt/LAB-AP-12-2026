while True:
    soal = int(input("Masukkan soal yang ingin dikerjakan (0 untuk selesai): "))
    if soal == 0:
        print("selesai")
        break

        #SOAL 1
    elif soal == 1:
        total_belanja = 0
        def sistem(harga, jumlah, adalah_member=False):
            harga_jumlah = harga * jumlah
            if adalah_member:
                harga_jumlah = harga_jumlah * (1 - 0.10)
                return int(harga_jumlah)
            return int(harga_jumlah)

        print("Selamat datang di kasir Minimarket!")
        while True:
            status_member = input("Apakah Anda member? (y/n): ")
            if status_member == "y":
                member = 1
                break
            elif status_member == "n":
                member = 2
                break
            else:
                print("Input yang anda masukkan tidak valid")
                continue

        while True:
            try:
                nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
                if nama_barang == "":
                    print(f"Total belanja: {total_belanja}")
                    break
                harga_barang = int(input("Harga barang: "))
                if harga_barang < 0:
                    raise ValueError("Input yang anda masukkan tidak valid")
                jumlah_barang = int(input("Jumlah barang: "))
                if member == 1:
                    subtotal = sistem(harga_barang, jumlah_barang, adalah_member=True)
                elif member == 2:
                    subtotal = sistem(harga_barang, jumlah_barang,)
                total_belanja += subtotal
                print(f"Subtotal {nama_barang}: {subtotal}")
            except:
                print("Input yang anda masukkan tidak valid")

        #SOAL 2
    elif soal == 2:
        def rekap_nilai(*nilai):
            rata_rata = sum(nilai) / len(nilai)
            nilai_tertinggi = max(nilai)
            nilai_terendah = min(nilai)

            return rata_rata, nilai_tertinggi, nilai_terendah


        nilai_siswa = []

        while True:
            input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")

            if input_nilai == "":
                break

            nilai_siswa.append(float(input_nilai))

        if len(nilai_siswa) == 0:
            print("Data nilai tidak tersedia.")
        else:
            rata, tertinggi, terendah = rekap_nilai(*nilai_siswa)

            print(f"Rata-rata kelas: {rata}")
            print(f"Nilai tertinggi: {tertinggi:g}")
            print(f"Nilai terendah: {terendah:g}")

        #SOAL 3
    elif soal == 3:
        def hitung_mundur(angka):
            if angka < 0:
                return

            print(angka)

            if angka == 0:
                print("Luncurkan!")
            else:
                hitung_mundur(angka - 1)


        while True:
            angka_awal = int(input("Masukkan angka awal hitung mundur: "))

            if angka_awal < 0:
                print("Input tidak valid, angka tidak boleh negatif.")
            else:
                break

        hitung_mundur(angka_awal)

        #SOAL 4
    elif soal == 4:
        def konversi(suhu, asal: str, tujuan: str):
            if asal == "C":
                if tujuan == "F":
                    nilai = (suhu * 1.8) + 32
                    return nilai
                elif tujuan == "K":
                    nilai = suhu + 273.15
                    return nilai
                else:
                    nilai = suhu
                    return nilai
            if asal == "F":
                if tujuan == "C":
                    nilai = (suhu - 32) * 5 / 9
                    return nilai
                if tujuan == "K":
                    nilai = (suhu -32) * 5 / 9 + 273.15
                    return nilai
                else:
                    nilai = suhu
                    return nilai
            if asal == "K":
                if tujuan == "C":
                    nilai = suhu - 273.15
                    return nilai
                if tujuan == "F":
                    nilai = (suhu - 273.15) * 1.8 + 32
                    return nilai
                else:
                    nilai = suhu
                    return nilai


        print("=== Konversi Suhu ===")
        while True:
            try:
                nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
                if nilai_suhu == "selesai":
                    break
                suhu = float(nilai_suhu)
                try:
                    skala_asal = input("Skala asal (C/F/K): ")
                    skala_tujuan = input("Skala tujuan (C/F/K): ")
                    if skala_asal != "C" and skala_asal != "F" and skala_asal != "K":
                        raise ValueError("Error")
                    if skala_tujuan != "C" and skala_tujuan != "F" and skala_tujuan != "K":
                        raise ValueError("Error")
                    konversi_akhir = konversi(suhu, skala_asal, skala_tujuan)
                    print(f"Hasil: {suhu} {skala_asal} = {konversi_akhir} {skala_tujuan}")
                except:
                    print("Error: Skala suhu tidak dikenali.")
                    continue
            except:
                print("Input yang anda masukkan tidak valid")
                continue

    else:
        print("soal tidak valid")
        continue