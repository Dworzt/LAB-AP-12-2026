jawaban = input ("masukkan nomor soal yang ingin di jalankan: ")
match jawaban:
    case "1":
        def hitung_subtotal(harga, jumlah, adalah_member=False):
            subtotal = harga * jumlah
            if adalah_member:
                subtotal *= 0.9  
            return int(subtotal)

        def soal_1():
            print("Selamat datang di Kasir Minimarket!")
            print()
            status_input = input("Apakah Anda member? (y/n): ").strip().lower()
            is_member = True if status_input == 'y'  else False
    
            total_belanja = 0
    
            while True:
                nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
                if nama_barang == "":
                    break
            
                try:
                    harga = int(input("Harga barang: "))
                    if harga < 0:
                        print("Harga tidak boleh negatif. Silakan masukkan harga yang valid.")
                        continue
                    elif harga == 0:
                        print("Harga tidak boleh nol. Silakan masukkan harga yang valid.")
                        continue
                except ValueError:
                    print("Input harga harus berupa angka!")
                    continue
        
                try:
                    jumlah = int(input("Jumlah barang: "))
                    if jumlah <= 0:
                        print("Jumlah barang harus berupa angka positif. Silakan masukkan jumlah yang valid.")
                        continue
                except ValueError:
                    print("Input jumlah harus berupa angka!")
                    continue
                subtotal = hitung_subtotal(harga, jumlah, adalah_member=is_member)
                print(f"Subtotal {nama_barang}: Rp{subtotal}")
        
                total_belanja += subtotal
        
            print(f"Total belanja: Rp{total_belanja}")
        soal_1()
    case "2":
        def hasil_akhir():
            print ("Pendataan nilai ujian siswa telah selesai, berikut hasil akhir:")
        def rekap_nilai(*args):
            if len(args) == 0:
                return None
    
            total = sum(args)
            rata_rata = total / len(args)
            tertinggi = max(args)
            terendah = min(args)
    
            return rata_rata, tertinggi, terendah

        daftar_nilai = []

        while True:
            
            inp = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
            try:
                if inp == "":
                    break

                if "." in inp:
                    nilai = float(inp)
                else:
                    nilai = int(inp)

                daftar_nilai.append(nilai)
                if len(daftar_nilai) <= 0:
                    print("Data nilai tidak tersedia.")
                           
                else:
                    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
                    continue
            except ValueError:
                print ("input data harus berupa angka!")
                continue
            finally:
                if inp == "":
                    hasil_akhir()
                    print(f"Rata-rata kelas: {rata}")
                    print(f"Nilai tertinggi: {tertinggi}")
                    print(f"Nilai terendah: {terendah}")
    case "3":
        import time
        def hitung_mundur (n):
            print(n)
            time.sleep(1)
            if n == 0:
                print ("Roket siap untuk diluncurkan!")
            else:
                hitung_mundur(n - 1)
        while True:
            n = int(input("masukkan angka awal hitung mundur: "))
            if n < 0:
                print ("angka tidak boleh negatif!")
                continue
            else:
                
                hitung_mundur(n)
                break

    case "4":
        def konversi_suhu_langsung(nilai, asal, tujuan):
            asal = asal.upper()
            tujuan = tujuan.upper()
            skala_valid = {"C", "F", "K"}

            if asal not in skala_valid or tujuan not in skala_valid:
                raise ValueError("ERROR! Skala suhu tidak dikenali.")

            if asal == tujuan:
                return nilai
            elif asal == "C" and tujuan == "F":
                return (nilai * 9/5) + 32
            elif asal == "C" and tujuan == "K":
                return nilai + 273.15
            elif asal == "F" and tujuan == "C":
                return (nilai - 32) * 5/9
            elif asal == "F" and tujuan == "K":
                return (nilai - 32) * 5/9 + 273.15
            elif asal == "K" and tujuan == "C":
                return nilai - 273.15
            elif asal == "K" and tujuan == "F":
                return (nilai - 273.15) * 9/5 + 32

        try:
            nilai = float(input("Masukkan nilai suhu: "))
            asal = input("Masukkan skala asal (C/F/K): ")
            tujuan = input("Masukkan skala tujuan (C/F/K): ")

            hasil = konversi_suhu_langsung(nilai, asal, tujuan)
            print(f"Hasil konversi: {nilai} °{asal.upper()} = {hasil:.2f} °{tujuan.upper()}")

        except ValueError as e:
            print(f"Error: {e}")            
