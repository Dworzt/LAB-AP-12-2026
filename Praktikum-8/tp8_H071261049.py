#1. Validasi Data Mahasiswa
import re
jawaban = input ("masukkan nomor soal yang akan dijalankan: ")
if jawaban == "1":
    def validasi_nim(nim):
        pola = r"^H071[0-9]{6,6}$"
        hasil = re.match(pola, nim)
        return hasil is not None

    def validasi_email(email):
        pola = r"^[A-Za-z0-9._]+@([A-Za-z0-9]+\.)+[A-Za-z]+$"
        hasil = re.match(pola, email)
        return hasil is not None

    def validasi_telepon(telepon):
        pola = r"^[0-9]{10,13}$"
        hasil = re.match(pola, telepon)
        return hasil is not None

    def main():
        print("=== Validasi Data Mahasiswa ===")
        print()

        nim_valid = False
        email_valid = False
        telepon_valid = False

        while True:
            if not nim_valid:
                nim = input("Masukkan NIM      : ").strip()
                if not nim:
                    print("NIM tidak boleh kosong!")
                    continue
                elif not validasi_nim(nim):
                    print("Format NIM tidak Valid!")
                    continue
                nim_valid = True

            if not email_valid:
                email = input("Masukkan Email    : ").strip()
                if not email:
                    print("Email tidak boleh kosong!")
                    continue
                elif not  validasi_email(email):
                    print("Format Email tidak Valid!")
                    continue
                email_valid = True

            if not telepon_valid:
                telepon = input("Masukkan No. Telp : ").strip()
                if not telepon:
                    print("Nomor telepon tidak boleh kosong!")
                    continue
                elif not validasi_telepon(telepon):
                    print("Format nomor telepon salah!")
                    continue
                telepon_valid = True

            
            break

        print()
        print("--- Hasil Validasi Akhir ---")
        print("NIM         : Valid")
        print("Email       : Valid")
        print("No. Telepon : Valid")
        print("\nData mahasiswa berhasil diverifikasi!")

    main()
elif jawaban == "2":


    def validasi_username(username):
        pola = r"^[A-Za-z][A-Za-z0-9_]{4,11}$"
        hasil = re.match(pola, username)
        return hasil is not None

    def main():
        daftar_valid = []
    
        print("=== Registrasi Username ===")
        print("Ketik 'SELESAI' untuk mengakhiri.")
        print()

        while True:
            try:
                username = input("Masukkan username: ").strip()

                if not username:
                    raise ValueError("Username tidak boleh kosong!")

                if not validasi_username(username):
                    raise ValueError("Username tidak valid!")

                if username in daftar_valid:
                    raise ValueError("Username sudah terdaftar.")
                
                if username.strip().upper() == "SELESAI":
                    break

                print("Username Tersedia.")
                print()
                daftar_valid.append(username)

            except ValueError as e:
                print(f"{e}\n")

        print()
        print("=== Rekapitulasi ===")
        if len(daftar_valid) == 0:
            print("Belum ada username yang valid.")
        else:
            print("Username valid:")
            nomor = 1
            for nama in daftar_valid:
                print(f"{nomor}. {nama}")
                nomor += 1
    
        print()
        print("Jumlah username valid:", len(daftar_valid))
    
    main()
elif jawaban == "3":


    def bersihkan_nomor(nomor):
        return re.sub(r"[^0-9]", "", nomor)

    def validasi_nomor(nomor_bersih):
        pola = r"^[0-9]{10,13}$"
        hasil = re.match(pola, nomor_bersih)
        return hasil is not None

    def main():
        print("=== Pembersihan Data Nomor Telepon ===")
        print()
        
        while True:
            try: 
                jumlah_data = int(input("Masukkan jumlah data: ").strip())
                print()
                
                if jumlah_data <= 0:
                    print("Jumlah harus lebih dari 0!")
                    continue

                break

            except ValueError:
                print("Inputan harus berupa angka bulat!")
                print()

        list_sebelum = []
        list_sesudah = []
        list_status = []
        list_nomor_valid = []

        no_input = 1
        while no_input <= jumlah_data:
            nomor_mentah = input("Nomor ke-" + str(no_input) + ": ").strip()
            
            nomor_bersih = bersihkan_nomor(nomor_mentah)
            list_sebelum.append(nomor_mentah)
            list_sesudah.append(nomor_bersih)
            
            if validasi_nomor(nomor_bersih):
                list_status.append("Valid")
                list_nomor_valid.append(nomor_bersih)
            else:
                list_status.append("Tidak valid")
                
            no_input = no_input + 1
            
        print()
        print("--- Hasil Pembersihan ---")
        print()
        
        no_cetak = 1
        for i in range(jumlah_data):
            print("Data " + str(no_cetak) + ":")
            print("Sebelum : " + list_sebelum[i])
            print("Sesudah : " + list_sesudah[i])
            print("Status  : " + list_status[i])
            print()
            no_cetak = no_cetak + 1
            
        print("Jumlah nomor valid:", len(list_nomor_valid))

    main()
else:
    print("nomor soal tidak valid")