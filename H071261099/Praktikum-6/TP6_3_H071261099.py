def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    print("=" * 55)
    print("No | Judul | Artis | Genre | Durasi")
    print("=" * 55)

    total_durasi = 0

    for i, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu

        menit = durasi // 60
        detik = durasi % 60

        print(
            i,
            "|", judul,
            "|", artis,
            "|", genre,
            "|", f"{menit}:{detik:02d}"
        )

        total_durasi += durasi

    print("=" * 55)

    total_menit = total_durasi // 60
    total_detik = total_durasi % 60

    print(
        "Total durasi playlist:",
        total_menit,
        "menit",
        total_detik,
        "detik"
    )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    indeks = nomor - 1

    if indeks < 0 or indeks >= len(playlist):
        print("Nomor lagu tidak valid.")
        return

    lagu = playlist.pop(indeks)

    print(f"Lagu '{lagu[0]}' berhasil dihapus.")


def statistik_playlist(playlist, genre_set):
    print("=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)

    total_lagu = len(playlist)

    print(f"Total lagu   : {total_lagu}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre not in distribusi:
            distribusi[genre] = 0

        distribusi[genre] += 1

    print()
    print("Distribusi genre:")

    for genre, jumlah in distribusi.items():
        print(genre, ":", jumlah)

    if len(playlist) > 0:
        lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
        lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

        durasi_panjang_menit = lagu_terpanjang[3] // 60
        durasi_panjang_detik = lagu_terpanjang[3] % 60

        durasi_pendek_menit = lagu_terpendek[3] // 60
        durasi_pendek_detik = lagu_terpendek[3] % 60

        print(
            "Lagu terpanjang:",
            lagu_terpanjang[0],
            "(",
            durasi_panjang_menit,
            ":",
            f"{durasi_panjang_detik:02d}",
            ")"
        )

        print(
            "Lagu terpendek:",
            lagu_terpendek[0],
            "(",
            durasi_pendek_menit,
            ":",
            f"{durasi_pendek_detik:02d}",
            ")"
        )

    print("=" * 40)


playlist = []
genre_set = set()

print("========================================")
print("       PLAYLIST MUSIK - PLAYTUNE")
print("========================================")

while True:
    print()
    print("Menu:")
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
        genre = input("Genre: ")

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
            else:
                tambah_lagu(
                    playlist,
                    genre_set,
                    judul,
                    artis,
                    genre,
                    durasi
                )

        except ValueError:
            print("Durasi harus berupa angka.")

    elif pilihan == "2":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Belum ada genre yang tersedia.")
        else:
            print("Genre tersedia:", genre_set)

            genre_target = input(
                "Masukkan genre yang ingin difilter: "
            )

            hasil = filter_genre(
                playlist,
                genre_target
            )

            if len(hasil) == 0:
                print("Tidak ada lagu dengan genre tersebut.")
            else:
                print(
                    "Lagu bergenre",
                    genre_target,
                    ":"
                )

                for i, lagu in enumerate(hasil, 1):
                    menit = lagu[3] // 60
                    detik = lagu[3] % 60

                    print(
                        i,
                        ".",
                        lagu[0],
                        "-",
                        lagu[1],
                        "(",
                        f"{menit}:{detik:02d}",
                        ")"
                    )

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)

            try:
                nomor = int(
                    input(
                        "Masukkan nomor lagu yang ingin dihapus: "
                    )
                )

                hapus_lagu(
                    playlist,
                    nomor
                )

            except ValueError:
                print("Nomor lagu harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(
            playlist,
            genre_set
        )

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid.")