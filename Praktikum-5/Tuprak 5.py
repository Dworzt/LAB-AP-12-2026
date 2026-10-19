jawaban = input("masukkan nomor soal yang akan dijalankan: ")
try:
    if "1" in jawaban:
        def bersihkan_teks(teks):
            alfabet = "abcdefghijklmnopqrstuvwxyz"
            hasil = ""
            for char in teks.lower():
                if char in alfabet:
                    hasil += char
            return hasil

        def cek_palinrome(teks):
            teks_dibalik = "".join(reversed(teks))
            if teks == teks_dibalik:
                return (True, -1)
    
    
            for i in range(len(teks)):
                if teks[i] != teks_dibalik[i]:
                    return (False, i)

        def inti_palinrome(teks):
            teks_bersih = bersihkan_teks(teks)
            n = len(teks_bersih)
    
            palindrom_terpanjang = ""
            indeks_awal = -1
            panjang_maks = 0
            
            for i in range(n):
                for j in range(i + 1, n + 1):
                    hasil_bersih = teks_bersih[i:j]
                    is_palin, _ = cek_palinrome(hasil_bersih)
            
                    if is_palin:
                        if len(hasil_bersih) > panjang_maks:
                            panjang_maks = len(hasil_bersih)
                            palindrom_terpanjang = hasil_bersih
                            indeks_awal = i
            
            print (input_teks)
            print ("Teks Bersih:", teks_bersih) 
            print (f"Output Terharap: ('teks': {panjang_maks}, 'panjang': {palindrom_terpanjang}, 'indeks awal': {indeks_awal})")  
             
            return {
                    "teks": palindrom_terpanjang,
                    "panjang": panjang_maks,
                    "indeks awal": indeks_awal
                }


        input_teks = input("Masukkan teks prasasti: ")
        if "" in input_teks:
            hasil = inti_palinrome(input_teks)
    if "2" in jawaban :
        def cek_kata (teks, kata):
            list_indeks = []
            kata_ = kata.lower()
            teks_awal = teks.lower()
            start = 0
            while True:
                indeks = teks_awal.find(kata_, start)
                if indeks == -1:
                    break
                list_indeks.append(indeks)
                start = indeks + 1
            return list_indeks
        def  cek_batas_kata (teks, i, panjang):
            alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if i > 0:
                if teks [i - 1] in alfabet :
                    return False
            indeks_sesudah = i + panjang
            if indeks_sesudah < len(teks):
                if teks[indeks_sesudah] in alfabet:
                    return False
            return True
        def sensor (teks, kata, simbol):
            indeks_total = cek_kata (teks, kata)
            panjang_kata = len(kata)

            indeks_valid= []
            for indeks in indeks_total:
                if cek_batas_kata(teks, indeks, panjang_kata):
                    indeks_valid.append(indeks)

            teks_Sensor = ""
            posisi_sekarang = 0
            for indeks in indeks_valid:
                teks_Sensor += teks[posisi_sekarang:indeks] + (simbol * panjang_kata)
                posisi_sekarang = indeks + panjang_kata
            teks_Sensor += teks[posisi_sekarang:]
            return (teks_Sensor, len(indeks_valid), indeks_valid)
        masukkan_teks = input ("Masukkan teks: ")
        Kata_target = input("Masukkan kata target: ")
        simbol_sensor = input ("Masukkan simbol: ")
        hasil_teks, jumlah, list_indeks = sensor(masukkan_teks, Kata_target, simbol_sensor)
        print(f"Hasil Teks: {hasil_teks}")
        print(f"Jumlah: {jumlah}  Indeks: {list_indeks}")
    if "3" in jawaban :
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        def cek_sandi (ch, k):
            return k.lower() in ch.lower()
        def deskripsi_ch (pesan, shift):
            hasil = ""
            for huruf in pesan:
                if huruf.lower() in alphabet:
                    idx = alphabet.find(huruf.lower())
                    idx_baru = (idx - shift)%26
                    hasil += alphabet[idx_baru]
                else:  
                    hasil += huruf
            return hasil     
        def brute_force(pesan, target):

            hasil = []

            for shift in range(26):

                dekripsi = deskripsi_ch(pesan, shift)

                if cek_sandi(dekripsi, target):
                    hasil.append([shift, dekripsi])

            return hasil


        pesan = input("Masukkan pesan terenkripsi: ")
        target = input("Masukkan kata kunci target: ")

        print("Output Dekripsi:", brute_force(pesan, target))

    if "4" in jawaban:
        def deteksi_anomali_email (email, daftar_email=None):
            error = []
            jumlah_at = email.count("@")
            if jumlah_at != 1:
                error.append("email harus memiliki tepat satu karakter @!")
                return error
            posisi_at = email.find("@")

            local = email[:posisi_at]
            domain = email[posisi_at + 1:]

            if local == "":
                error.append("bagian local sebelum @ tidak boleh kosong.")

            if domain == "":
                error.append("bagian domain setelah @ tidak boleh kosong.")

            if " " in email:
                error.append("email tidak boleh mengandung spasi.")

    
            if local != "":
                if local[0] == ".":
                    error.append("bagian local tidak boleh diawali titik.")

                if local[-1] == ".":
                    error.append("bagian local tidak boleh diakhiri titik.")

                if ".." in local:
                    error.append("bagian local tidak boleh memiliki titik berurutan.")

    
            if domain != "":
                if "." not in domain:
                    error.append("bagian domain harus memiliki minimal satu titik.")

                if ".." in domain:
                    error.append("bagian domain tidak boleh memiliki titik berurutan.")

                if domain[-1] == ".":
                    error.append("bagian domain tidak boleh diakhiri titik.")

        
                if not domain.lower().endswith((".com", ".id", ".ac.id")):
                    error.append(
                        "email harus berakhiran .com, .id, atau .ac.id."
                    )

    
            if daftar_email is not None:
                for email_lama in daftar_email:
                    if email_lama.lower() == email.lower():
                        error.append("email tidak boleh duplikat.")
                        break

            return error


        def cetak_daftar(daftar_email, karakter_border):
            if len(daftar_email) == 0:
                return "belum ada email valid."

            panjang_terpanjang = 0


            for email in daftar_email:
                if len(email) > panjang_terpanjang:
                    panjang_terpanjang = len(email)

            lebar = panjang_terpanjang + 4
            border = karakter_border * (lebar + 2)

            hasil = ""
            hasil += border + "\n"

            for email in daftar_email:
                jumlah_spasi = panjang_terpanjang - len(email)

                hasil += karakter_border
                hasil += " " + email + (" " * jumlah_spasi) + " "
                hasil += karakter_border
                hasil += "\n"

            hasil += border

            return hasil



        daftar_email = []

        print("=== VALIDASI EMAIL ===")
        print("ketik 'tutup' untuk mengakhiri.")

        while True:
            email = input("\nmasukkan email: ")

            if email.lower() == "tutup":
                break

            error = deteksi_anomali_email(
                email,
                daftar_email
            )

            if len(error) == 0:
                daftar_email.append(email)

                print("\nemail valid!")
                print(cetak_daftar(daftar_email, "="))

            else:
                print("\nemail tidak valid.")
                print("alasan:")

                for nomor, pesan_error in enumerate(error, start=1):
                        print(str(nomor) + ". " + pesan_error)


        print("\nprogram selesai.")
        print("daftar email valid:")
        print(cetak_daftar(daftar_email, "="))
 
except ValueError:
    print ("nomor soal tidak sesuai output yang tersedia.")        
