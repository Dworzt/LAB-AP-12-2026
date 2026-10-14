while True:
    soal = int(input("Masukkan soal yang ingin dikerjakan (0 untuk selesai): "))
    if soal == 0:
        print("selesai")
        break

        #SOAL 1
    elif soal == 1:
        def tambah_buku(inventaris, judul, penulis, harga, stok):
            buku = {
                "judul": judul,
                "penulis": penulis,
                "harga": harga,
                "stok": stok
            }
            inventaris.append(buku)
            print(f"Buku '{judul}' berhasil ditambahkan!")


        def cari_buku(inventaris, kata_kunci):
            hasil = []
            for buku in inventaris:
                if kata_kunci.lower() in buku["judul"].lower():
                    hasil.append(buku)

            if len(hasil) == 0:
                print("Buku tidak ditemukan.")
            else:
                print(f"Ditemukan {len(hasil)} buku:")
                for nomor, buku in enumerate(hasil, start=1):
                    print(
                        f"  {nomor}. {buku['judul']} - {buku['penulis']} | "
                        f"Rp{buku['harga']:g} | Stok: {buku['stok']}"
                    )


        def update_stok(inventaris, judul, jumlah):
            for buku in inventaris:
                if buku["judul"].lower() == judul.lower():
                    stok_baru = buku["stok"] + jumlah

                    if stok_baru < 0:
                        print("Gagal: stok tidak boleh menjadi negatif.")
                        return

                    buku["stok"] = stok_baru

                    if jumlah > 0:
                        print(
                            f"Stok '{buku['judul']}' bertambah {jumlah}. "
                            f"Stok sekarang: {buku['stok']}"
                        )
                    elif jumlah < 0:
                        print(
                            f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. "
                            f"Stok sekarang: {buku['stok']}"
                        )
                    else:
                        print(f"Tidak ada perubahan. Stok sekarang: {buku['stok']}")
                    return

            print(f"Error: buku '{judul}' tidak ditemukan.")


        def ringkasan_inventaris(inventaris):
            print("=" * 40)
            print("RINGKASAN INVENTARIS BOOKNEST")
            print("=" * 40)

            jumlah_jenis = len(inventaris)
            total_stok = 0
            total_aset = 0

            for buku in inventaris:
                total_stok += buku["stok"]
                total_aset += buku["harga"] * buku["stok"]

            print(f"Jumlah jenis buku : {jumlah_jenis}")
            print(f"Total seluruh stok: {total_stok}")
            print(f"Total nilai aset  : Rp{total_aset:g}")

            if len(inventaris) > 0:
                buku_termahal = inventaris[0]
                for buku in inventaris:
                    if buku["harga"] > buku_termahal["harga"]:
                        buku_termahal = buku
                print(
                    f"Buku termahal     : {buku_termahal['judul']} "
                    f"(Rp{buku_termahal['harga']:g})"
                )
            else:
                print("Buku termahal     : Belum ada buku")

            print("=" * 40)


        inventaris = []

        opening = "SISTEM INVENTARIS TOKO BUKU BOOKNEST"
        strip = len(opening) + 4

        print("=" * strip)
        print(opening.center(len(opening) + 4))
        print("=" * strip)
        print(" ")

        while True:
            print("Menu:")
            print("1. Tambah Buku")
            print("2. Cari Buku")
            print("3. Update Stok")
            print("4. Ringkasan Inventaris")
            print("5. Keluar")

            pilihan = input("Pilih menu (1-5): ").strip()

            if pilihan == "1":
                judul = input("Judul buku: ").strip()
                penulis = input("Penulis: ").strip()

                if judul == "" or penulis == "":
                    print("Judul dan penulis tidak boleh kosong.")
                    continue

                try:
                    harga = float(input("Harga: "))
                    stok = int(input("Stok awal: "))

                    if harga < 0 or stok < 0:
                        print("Harga dan stok tidak boleh negatif.")
                        continue

                except ValueError:
                    print("Harga harus berupa angka dan stok harus berupa bilangan bulat.")
                    continue

                tambah_buku(inventaris, judul, penulis, harga, stok)

            elif pilihan == "2":
                kata_kunci = input("Masukkan kata kunci judul: ").strip()
                cari_buku(inventaris, kata_kunci)

            elif pilihan == "3":
                judul = input("Judul buku yang ingin diupdate: ").strip()

                try:
                    jumlah = int(
                        input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
                    )
                except ValueError:
                    print("Jumlah perubahan harus berupa bilangan bulat.")
                    continue

                update_stok(inventaris, judul, jumlah)

            elif pilihan == "4":
                ringkasan_inventaris(inventaris)

            elif pilihan == "5":
                print("Terima kasih telah menggunakan BookNest!")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka 1 sampai 5.")

        #SOAL 2
    elif soal == 2:
        def daftar_kandidat(kandidat_set, nama):
            """Mendaftarkan kandidat dengan format capitalize dan tanpa duplikasi."""
            nama = nama.strip().capitalize()
            if nama == "":
                return False
            if nama in kandidat_set:
                print(f"'{nama}' sudah terdaftar sebagai kandidat.")
                return False
            kandidat_set.add(nama)
            print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
            return True


        def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
            """Mencatat suara jika pemilih belum memilih dan kandidat valid."""
            nama_asli = nama_pemilih.strip()
            pemilih_key = nama_asli.lower()
            pilihan = pilihan.strip().capitalize()

            if pemilih_key in rekap_suara:
                print(f"'{nama_asli}' sudah memberikan suara sebelumnya!")
                return False
            if pilihan not in kandidat_set:
                print(f"Error: kandidat '{pilihan}' tidak terdaftar. Suara tidak dicatat.")
                return False

            rekap_suara[pemilih_key] = pilihan
            print(f"Suara '{nama_asli}' untuk '{pilihan}' berhasil dicatat!")
            return True


        def hitung_suara(rekap_suara, kandidat_set):
            """Menghitung jumlah suara untuk setiap kandidat."""
            perolehan = {}
            for kandidat in kandidat_set:
                perolehan[kandidat] = 0
            for pilihan in rekap_suara.values():
                perolehan[pilihan] += 1
            return perolehan


        def tampilkan_hasil(perolehan):
            """Menampilkan hasil pemilihan dan menentukan pemenang atau seri."""
            print("\n" + "=" * 40)
            print("HASIL PEMILIHAN KETUA KELAS".center(40))
            print("=" * 40)

            for kandidat in sorted(perolehan):
                print(f"  {kandidat}: {perolehan[kandidat]} suara")

            total_suara = sum(perolehan.values())
            print(f"\nTotal suara masuk: {total_suara}")

            if len(perolehan) == 0:
                print("Tidak ada kandidat yang dapat diumumkan.")
            else:
                suara_tertinggi = max(perolehan.values())
                kandidat_tertinggi = [
                    nama for nama, jumlah in perolehan.items()
                    if jumlah == suara_tertinggi
                ]
                if len(kandidat_tertinggi) > 1:
                    print("Hasil SERI antara: " + ", ".join(sorted(kandidat_tertinggi)))
                    print("Perlu dilakukan pemilihan ulang!")
                else:
                    print(
                        f"PEMENANG: {kandidat_tertinggi[0]} "
                        f"dengan {suara_tertinggi} suara!"
                    )
            print("=" * 40)


        kandidat_set = set()
        rekap_suara = {}

        opening = "SISTEM PEMILIHAN KETUA KELAS"
        strip = len(opening) + 4

        print("=" * strip)
        print(opening.center(len(opening) + 4))
        print("=" * strip)
        print(" ")

        print("\n--- FASE PENDAFTARAN KANDIDAT ---")
        while True:
            nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
            if nama == "":
                if len(kandidat_set) >= 2:
                    break
                print("Minimal harus ada 2 kandidat. Silakan daftarkan kandidat lagi.")
                continue
            daftar_kandidat(kandidat_set, nama)

        print("\nKandidat terdaftar:", kandidat_set)
        print("\n--- FASE PEMUNGUTAN SUARA ---")

        while True:
            nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ").strip()
            if nama_pemilih == "":
                break
            print("Kandidat yang tersedia:", kandidat_set)
            pilihan = input("Pilih kandidat: ")
            berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

        perolehan = hitung_suara(rekap_suara, kandidat_set)
        tampilkan_hasil(perolehan)

        #SOAL 3
    elif soal == 3:
        def format_durasi(durasi_detik):
            menit = durasi_detik // 60
            detik = durasi_detik % 60
            return f"{menit}:{detik:02d}"


        def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
            lagu = (judul, artis, genre.capitalize(), durasi)
            playlist.append(lagu)
            genre_set.add(lagu[2])
            print(f"Lagu '{lagu[0]}' oleh {lagu[1]} berhasil ditambahkan!")


        def tampilkan_playlist(playlist):
            print("\n" + "=" * 78)
            print(f"{'No':<4}{'Judul':<25}{'Artis':<20}{'Genre':<12}{'Durasi':>8}")
            print("=" * 78)

            total_durasi = 0
            for nomor, lagu in enumerate(playlist, start=1):
                judul, artis, genre, durasi = lagu
                print(
                    f"{nomor:<4}{judul[:24]:<25}{artis[:19]:<20}"
                    f"{genre[:11]:<12}{format_durasi(durasi):>8}"
                )
                total_durasi += durasi

            print("=" * 78)
            total_menit = total_durasi // 60
            sisa_detik = total_durasi % 60
            print(f"Total durasi playlist: {total_menit} menit {sisa_detik} detik")
            return total_durasi


        def filter_genre(playlist, genre_target):
            return [
                lagu for lagu in playlist
                if lagu[2].lower() == genre_target.strip().capitalize().lower()
            ]


        def hapus_lagu(playlist, nomor):
            if nomor < 1 or nomor > len(playlist):
                print("Nomor lagu tidak valid.")
                return False

            lagu = playlist.pop(nomor - 1)
            print(f"Lagu '{lagu[0]}' berhasil dihapus dari playlist.")
            return True


        def statistik_playlist(playlist, genre_set):
            print("\n" + "=" * 40)
            print("STATISTIK PLAYLIST PLAYTUNE".center(40))
            print("=" * 40)
            print(f"Total lagu      : {len(playlist)}")
            print(f"Jumlah genre    : {len(genre_set)}")
            print(f"Daftar genre    : {genre_set}")

            distribusi = {}
            for lagu in playlist:
                genre = lagu[2]
                if genre in distribusi:
                    distribusi[genre] += 1
                else:
                    distribusi[genre] = 1

            print("\nDistribusi genre:")
            if len(distribusi) == 0:
                print("  Belum ada lagu.")
            else:
                for genre in sorted(distribusi):
                    print(f"  {genre:<12}: {'#' * distribusi[genre]} ({distribusi[genre]})")

            if len(playlist) > 0:
                lagu_terpanjang = playlist[0]
                lagu_terpendek = playlist[0]

                for lagu in playlist:
                    if lagu[3] > lagu_terpanjang[3]:
                        lagu_terpanjang = lagu
                    if lagu[3] < lagu_terpendek[3]:
                        lagu_terpendek = lagu

                print(
                    f"\nLagu terpanjang : {lagu_terpanjang[0]} "
                    f"({format_durasi(lagu_terpanjang[3])})"
                )
                print(
                    f"Lagu terpendek  : {lagu_terpendek[0]} "
                    f"({format_durasi(lagu_terpendek[3])})"
                )
            else:
                print("\nLagu terpanjang : Belum ada lagu")
                print("Lagu terpendek  : Belum ada lagu")

            print("=" * 40)


        playlist = []
        genre_set = set()

        print("=" * 40)
        print("PLAYLIST MUSIK - PLAYTUNE".center(40))
        print("=" * 40)

        while True:
            print("\nMenu:")
            print("1. Tambah Lagu")
            print("2. Tampilkan Playlist")
            print("3. Filter berdasarkan Genre")
            print("4. Hapus Lagu")
            print("5. Statistik Playlist")
            print("6. Keluar")

            pilihan = input("Pilih menu (1-6): ").strip()

            if pilihan == "1":
                judul = input("Judul lagu: ").strip()
                artis = input("Artis: ").strip()
                genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip()

                if judul == "" or artis == "" or genre == "":
                    print("Judul, artis, dan genre tidak boleh kosong.")
                    continue

                try:
                    durasi = int(input("Durasi (dalam detik): "))
                    if durasi <= 0:
                        print("Durasi harus berupa angka positif.")
                        continue
                except ValueError:
                    print("Durasi harus berupa angka bulat.")
                    continue

                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)

            elif pilihan == "2":
                tampilkan_playlist(playlist)

            elif pilihan == "3":
                print("Genre tersedia:", genre_set)
                genre_target = input("Masukkan genre yang ingin difilter: ")
                hasil_filter = filter_genre(playlist, genre_target)

                if len(hasil_filter) == 0:
                    print("Tidak ada lagu untuk genre tersebut.")
                else:
                    print(f"\nLagu bergenre '{genre_target.strip().capitalize()}':")
                    for nomor, lagu in enumerate(hasil_filter, start=1):
                        print(
                            f"  {nomor}. {lagu[0]} - {lagu[1]} "
                            f"({format_durasi(lagu[3])})"
                        )

            elif pilihan == "4":
                if len(playlist) == 0:
                    print("Playlist masih kosong, tidak ada lagu yang dapat dihapus.")
                    continue

                tampilkan_playlist(playlist)
                try:
                    nomor = int(input("Nomor lagu yang ingin dihapus: "))
                except ValueError:
                    print("Nomor lagu harus berupa angka bulat.")
                    continue

                berhasil = hapus_lagu(playlist, nomor)

                if berhasil:
                    genre_set.clear()
                    for lagu in playlist:
                        genre_set.add(lagu[2])

            elif pilihan == "5":
                statistik_playlist(playlist, genre_set)

            elif pilihan == "6":
                print("Terima kasih telah menggunakan PlayTune!")
                break

            else:
                print("Pilihan tidak valid. Masukkan angka 1 sampai 6.")

    else:
        print("soal tidak valid")
        continue