while True:
    soal = int(input("Masukkan soal yang ingin dikerjakan (0 untuk selesai): "))
    if soal == 0:
        print("selesai")
        break

        #SOAL 1
    elif soal == 1:
        
        huruf = "abcdefghijklmnopqrstuvwxyz"

        def bersihkan_teks(text):
            simpan = ""
            for i in text:
                if i in huruf:
                    simpan += i
            return simpan

        def cek_palinrome(text):
            teks_terbalik = "".join(reversed(text))
            panjang_teks = len(text)
            for i in range(panjang_teks):
                if text[i] != teks_terbalik[i]:
                    return (False, i)
            return (True, -1)

        def inti_palinrome(text):
            teks_bersih = bersihkan_teks(text)
            palinrome_terpanjang = ""
            panjang_teks = len(teks_bersih)
            for i in range(panjang_teks):
                for j in range(i + 1, panjang_teks + 1):
                    potongan = teks_bersih[i:j]
                    palinrome = cek_palinrome(potongan)[0]
                    if palinrome:
                        if len(potongan) > len(palinrome_terpanjang):
                            palinrome_terpanjang = potongan
                            indeks_awal = i
            return {
                "teks": palinrome_terpanjang,
                "panjang": len(palinrome_terpanjang),
                "indek_awal": indeks_awal
            }

        input_kata = input("Masukkan teks prasasti: "). lower()
        tes = inti_palinrome(input_kata)
        bersih = bersihkan_teks(input_kata)
        print(f"Teks Bersih: {bersih}")
        print(f"Output Terharap: {tes}")


        #SOAL 2
    elif soal == 2:

        huruf = "abcdefghijklmnopqrstuvwxyz"

        def cek_kata(teks, kata):
            indeks_list = []
            start = 0
            while True:
                posisi = teks.find(kata, start)
                if posisi == -1:
                    break
                indeks_list.append(posisi)
                start = posisi + 1
            return indeks_list

        def cek_batas_kata(teks, i, panjang):
            if i > 0:
                kata_sebelum = teks[i - 1]
                if kata_sebelum == huruf or kata_sebelum == huruf.upper():
                    return False
            if i + panjang < len(teks):
                kata_sesudah = teks[i + panjang]
                if kata_sesudah == huruf or kata_sesudah == huruf.upper():
                    return False
            return True

        def sensor_kata(teks, kata, simbol):
            panjang = len(kata)
            indeks_kemunculan = cek_kata(teks, kata)
            indeks_valid = [i for i in indeks_kemunculan if cek_batas_kata(teks, i, panjang)]
            teks_akhir = ""
            last_idx = 0
            pengganti = simbol * panjang
            
            for idx in indeks_valid:
                teks_akhir += teks[last_idx:idx] + pengganti
                last_idx = idx + panjang
                
            teks_akhir += teks[last_idx:]
            
            return teks_akhir, len(indeks_valid), indeks_valid


        teks = input("Masukkan Teks: ").lower ()
        kata_target = input("Masukkan kata target: ").lower ()
        simbol = input("Masukkan simbol: ")

        teks_baru, jumlah, daftar_indeks = sensor_kata(teks, kata_target, simbol)

        print(f"Hasil Sensor  : {teks_baru}")
        print(f"Jumlah Tersensor : {jumlah}")
        print(f"Indeks Awal      : {daftar_indeks}")

        #SOAL 3
    elif soal == 3:

        ALFABET = "abcdefghijklmnopqrstuvwxyz"

        def cek_sandi(ch, k):
            is_upper = ch.isupper()
            ch_lower = ch.lower()    
            idx = ALFABET.find(ch_lower)
            if idx == -1:
                return ch
            
            idx_baru = (idx + k) % 26
            huruf_baru = ALFABET[idx_baru]
            
            if is_upper:
                return huruf_baru.upper()
            return huruf_baru

        def mesin_enkripsi(teks, k):
            hasil = ""
            for ch in teks:
                hasil += cek_sandi(ch, k)
            return hasil

        def mesin_dekripsi(teks, k):
            return mesin_enkripsi(teks, -k)

        def retas_sandi(sandi, kata_kunci):
            hasil_retas = []
            for k in range(26):
                teks_dekripsi = mesin_dekripsi(sandi, k)
                if teks_dekripsi.lower().find(kata_kunci.lower()) != -1:
                    hasil_retas.append((k, teks_dekripsi))
                    
            return hasil_retas

        pesan_tersita = input("Masukkan pesan tersita (enkripsi Caesar): ")
        kata_kunci_target = input("Masukkan kata kunci target: ")

        output = retas_sandi(pesan_tersita, kata_kunci_target)
        print("Output Deskripsi:", output)

        #SOAL 4
    elif soal == 4:

        database_email = []
        domain_list = (".com", ".id", ".ac.id",)

        def deteksi_anomali_email(email):
            list_error = []
            if " " in email:
                list_error.append("Email tidak boleh memiliki spasi")
            if email.count("@") != 1:
                list_error.append("Harus memiliki tepat satu karakter @")
                return list_error

            local, domain = email.split("@")

            if not local or not domain:
                list_error.append("Bagian sebelum @ (local) atau setelah @ (domai) tidak boleh kosong")

            if local:
                if local.startswith(".") or local.endswith("."):
                    list_error.append("Bagian local tidak boleh diawali atau diakhiri titik, serta tidak boleh mengandung titik berurutan")
                if ".." in local:
                    list_error.append("Bagian local tidak boleh diawali atau diakhiri titik, serta tidak boleh mengandung titik berurutan")

            if domain:
                if not "." in domain:
                    list_error.append("Bagian domain wajib memiliki minimal satu titik")
                if ".." in domain:
                    list_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
                if domain.endswith("."):
                    list_error.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
                if domain.startswith("."):
                    list_error.append("Bagian setelah domain(@) tidak boleh kosong")

            if not email.lower().endswith(domain_list):
                list_error.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

            if not list_error and email in database_email:
                list_error.append("Email sudah terdaftar (Duplikat)")

            return list_error

        def cetak_daftar(daftar_email_valid, karakter_border):
            if not database_email:
                return ""
            email_terpanjang = max(len(email) for email in database_email)
            lebar_garis = email_terpanjang + 2
            garis_horizontal = karakter_border * lebar_garis

            hasil_bingkai = [f"+{garis_horizontal}+"]
            for email in daftar_email_valid:
                baris = f"| {email.ljust(email_terpanjang)} |"
                hasil_bingkai.append(baris)
            hasil_bingkai.append(f"+{garis_horizontal}+")

            return "\n".join(hasil_bingkai)

        print("--- Sistem Pencatatan email valid ---")
        border = input("Masukkan border dengan karakter bebas: ")

        print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")
        while True:
            user = input("Masukkan email: ")
            email_bersih = deteksi_anomali_email(user)
            if user == "tutup":
                break
            if not email_bersih:
                database_email.append(user.lower())
                print("Email VALID!")
            else:
                print("Email DITOLAK karena:")
                for error in email_bersih:
                    print(f"   - {error}")

        print()
        print("--- HASIL EMAIL VALID ---")
        if database_email:
                bingkai_teks = cetak_daftar(database_email, border)
                print(bingkai_teks)
                print()
        else:
            print("(Tidak ada email valid yang terdaftar)")

    else:
        print("soal tidak valid")
        continue