#Soal 1
def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }

    inventaris.append(buku)
    print("Buku", judul, "berhasil ditambahkan!")


def cari_buku(inventaris, kata_kunci):
    ditemukan = False

    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            print(
                buku["judul"], "-", buku["penulis"],
                "| Rp", buku["harga"],
                "| Stok:", buku["stok"]
            )
            ditemukan = True

    if ditemukan == False:
        print("Buku tidak ditemukan.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Error: Stok tidak boleh negatif.")
            else:
                buku["stok"] = stok_baru

                if jumlah > 0:
                    print("Stok", buku["judul"],
                          "bertambah", jumlah,
                          "Stok sekarang:", stok_baru)
                elif jumlah < 0:
                    print("Stok", buku["judul"],
                          "berkurang", abs(jumlah),
                          "Stok sekarang:", stok_baru)
                else:
                    print("Stok tidak berubah.")

            return

    print("Error: Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    jumlah_buku = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = None

    for buku in inventaris:
        total_stok = total_stok + buku["stok"]
        total_aset = total_aset + (
            buku["harga"] * buku["stok"]
        )

        if buku_termahal is None:
            buku_termahal = buku
        elif buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku

    print("\n========================================")
    print("       RINGKASAN INVENTARIS BOOKNEST")
    print("========================================")
    print("Jumlah jenis buku :", jumlah_buku)
    print("Total seluruh stok:", total_stok)
    print("Total nilai aset  : Rp", total_aset)

    if buku_termahal is not None:
        print("Buku termahal     :",
              buku_termahal["judul"],
              "(Rp" + str(buku_termahal["harga"]) + ")")
    else:
        print("Buku termahal     : Belum ada buku")

    print("========================================")


inventaris = []

while True:
    print("\n========================================")
    print("      SISTEM INVENTARIS TOKO BUKU")
    print("               BOOKNEST")
    print("========================================")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")

        try:
            harga = float(input("Harga: "))
            stok = int(input("Stok awal: "))

            if harga < 0 or stok < 0:
                print("Error: Harga dan stok tidak boleh negatif.")
            else:
                tambah_buku(
                    inventaris, judul, penulis, harga, stok
                )

        except ValueError:
            print("Error: Harga dan stok harus berupa angka.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")

        try:
            jumlah = int(
                input("Jumlah perubahan (positif=tambah, negatif=kurang): ")
            )
            update_stok(inventaris, judul, jumlah)

        except ValueError:
            print("Error: Jumlah perubahan harus berupa angka.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-5.")


#soal 2
def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()

    if nama in kandidat_set:
        print("Kandidat", nama, "sudah terdaftar.")
    else:
        kandidat_set.add(nama)
        print("Kandidat", nama, "berhasil didaftarkan!")


def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()

    if nama_pemilih in rekap_suara:
        print("Pemilih ini sudah memberikan suara sebelumnya!")
        return

    if pilihan not in kandidat_set:
        print("Error: Kandidat tidak terdaftar.")
        return

    rekap_suara[nama_pemilih] = pilihan

    print("Suara berhasil dicatat untuk", pilihan + "!")


def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}

    for kandidat in kandidat_set:
        perolehan[kandidat] = 0

    for pilihan in rekap_suara.values():
        perolehan[pilihan] = perolehan[pilihan] + 1

    return perolehan


def tampilkan_hasil(perolehan):
    print("\n========================================")
    print("       HASIL PEMILIHAN KETUA KELAS")
    print("========================================")

    total_suara = 0

    for kandidat in perolehan:
        print(kandidat + ":", perolehan[kandidat], "suara")
        total_suara = total_suara + perolehan[kandidat]

    print("\nTotal suara masuk:", total_suara)

    if total_suara == 0:
        print("Belum ada suara yang masuk.")
    else:
        suara_tertinggi = max(perolehan.values())
        pemenang = []

        for kandidat in perolehan:
            if perolehan[kandidat] == suara_tertinggi:
                pemenang.append(kandidat)

        if len(pemenang) > 1:
            print("Hasil SERI antara:", ", ".join(pemenang))
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print("PEMENANG:", pemenang[0],
                  "dengan", suara_tertinggi, "suara!")

    print("========================================")


kandidat_set = set()
rekap_suara = {}

print("========================================")
print("   SISTEM PEMILIHAN KETUA KELAS")
print("              VOTECLASS")
print("========================================")

print("\n--- FASE PENDAFTARAN KANDIDAT ---")

while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        break

    daftar_kandidat(kandidat_set, nama)

while len(kandidat_set) < 2:
    print("Minimal harus ada 2 kandidat!")

    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")

    if nama == "":
        print("Pendaftaran belum bisa dilanjutkan.")
        continue

    daftar_kandidat(kandidat_set, nama)

print("\nKandidat terdaftar:", kandidat_set)
print("\n--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input(
        "\nNama pemilih (kosongkan untuk selesai): "
    )

    if nama_pemilih == "":
        break

    print("Kandidat yang tersedia:", kandidat_set)

    pilihan = input("Pilih kandidat: ")

    berikan_suara(
        rekap_suara, kandidat_set, nama_pemilih, pilihan
    )

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)


#soal 3
def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)

    playlist.append(lagu)
    genre_set.add(genre)

    print("Lagu", judul, "oleh", artis,
          "berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    print("\n==============================================================")
    print("No  Judul                  Artis              Genre      Durasi")
    print("==============================================================")

    total_durasi = 0

    if len(playlist) == 0:
        print("Playlist masih kosong.")

    for i in range(len(playlist)):
        lagu = playlist[i]

        menit = lagu[3] // 60
        detik = lagu[3] % 60

        waktu = str(menit) + ":" + str(detik).zfill(2)

        print(
            i + 1,
            lagu[0],
            "-",
            lagu[1],
            "-",
            lagu[2],
            "-",
            waktu
        )

        total_durasi = total_durasi + lagu[3]

    total_menit = total_durasi // 60
    total_detik = total_durasi % 60

    print("==============================================================")
    print("Total durasi playlist:",
          total_menit, "menit", total_detik, "detik")


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Error: Nomor lagu tidak valid.")
    else:
        lagu = playlist.pop(nomor - 1)
        print("Lagu", lagu[0], "berhasil dihapus.")


def statistik_playlist(playlist, genre_set):
    print("\n========================================")
    print("       STATISTIK PLAYLIST PLAYTUNE")
    print("========================================")

    print("Total lagu  :", len(playlist))
    print("Jumlah genre:", len(genre_set))
    print("Daftar genre:", genre_set)

    distribusi = {}

    for genre in genre_set:
        distribusi[genre] = 0

    for lagu in playlist:
        distribusi[lagu[2]] = distribusi[lagu[2]] + 1

    print("\nDistribusi genre:")

    for genre in distribusi:
        print(genre, ":", distribusi[genre], "lagu")

    if len(playlist) > 0:
        lagu_terpanjang = playlist[0]
        lagu_terpendek = playlist[0]

        for lagu in playlist:
            if lagu[3] > lagu_terpanjang[3]:
                lagu_terpanjang = lagu

            if lagu[3] < lagu_terpendek[3]:
                lagu_terpendek = lagu

        menit_panjang = lagu_terpanjang[3] // 60
        detik_panjang = lagu_terpanjang[3] % 60

        menit_pendek = lagu_terpendek[3] // 60
        detik_pendek = lagu_terpendek[3] % 60

        print("\nLagu terpanjang:",
              lagu_terpanjang[0],
              "(" + str(menit_panjang) + ":" +
              str(detik_panjang).zfill(2) + ")")

        print("Lagu terpendek :",
              lagu_terpendek[0],
              "(" + str(menit_pendek) + ":" +
              str(detik_pendek).zfill(2) + ")")
    else:
        print("Belum ada lagu dalam playlist.")

    print("========================================")


playlist = []
genre_set = set()

while True:
    print("\n========================================")
    print("       PLAYLIST MUSIK - PLAYTUNE")
    print("========================================")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Error: Durasi harus lebih dari 0.")
            else:
                tambah_lagu(
                    playlist, genre_set,
                    judul, artis, genre, durasi
                )

        except ValueError:
            print("Error: Durasi harus berupa angka.")

    elif pilihan == "2":
        tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Belum ada genre yang tersedia.")
        else:
            print("Genre tersedia:", genre_set)

            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            )

            hasil = filter_genre(playlist, genre_target)

            if len(hasil) == 0:
                print("Tidak ada lagu dengan genre tersebut.")
            else:
                print("\nLagu dengan genre", genre_target + ":")

                for i in range(len(hasil)):
                    lagu = hasil[i]

                    menit = lagu[3] // 60
                    detik = lagu[3] % 60

                    print(
                        i + 1, lagu[0], "-",
                        lagu[1], "(",
                        str(menit) + ":" +
                        str(detik).zfill(2), ")"
                    )

    elif pilihan == "4":
        tampilkan_playlist(playlist)

        if len(playlist) > 0:
            try:
                nomor = int(
                    input("Masukkan nomor lagu yang ingin dihapus: ")
                )

                hapus_lagu(playlist, nomor)

            except ValueError:
                print("Error: Nomor harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")

        