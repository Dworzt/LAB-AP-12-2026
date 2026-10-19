playlist = []


def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"


while True:
    print("\n======================================")
    print("      PLAYLIST MUSIK - PLAYTUNE")
    print("======================================")

    print("\nMenu:")
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

            lagu = {
                "judul": judul,
                "artis": artis,
                "genre": genre,
                "durasi": durasi
            }

            playlist.append(lagu)

            print(
                f"Lagu '{judul}' oleh "
                f"{artis} berhasil ditambahkan!"
            )

        except ValueError:
            print("Durasi harus berupa angka.")

    elif pilihan == "2":

        if not playlist:
            print("Playlist kosong.")
            continue

        print("\n======================================================")
        print("No  Judul                Artis         Genre   Durasi")
        print("======================================================")

        total_durasi = 0

        for i, lagu in enumerate(playlist, start=1):
            print(
                f"{i:<3}"
                f"{lagu['judul']:<20}"
                f"{lagu['artis']:<14}"
                f"{lagu['genre']:<8}"
                f"{format_durasi(lagu['durasi'])}"
            )

            total_durasi += lagu["durasi"]

        print("======================================================")

        menit = total_durasi // 60
        detik = total_durasi % 60

        print(
            f"Total durasi playlist: "
            f"{menit} menit {detik} detik"
        )

    elif pilihan == "3":

        genre_unik = {
            lagu["genre"]
            for lagu in playlist
        }

        print(f"Genre tersedia: {genre_unik}")

        genre_cari = input(
            "Masukkan genre yang ingin difilter: "
        )

        hasil = [
            lagu
            for lagu in playlist
            if lagu["genre"].lower()
            == genre_cari.lower()
        ]

        if hasil:

            print(f"\nLagu bergenre '{genre_cari}':")

            for i, lagu in enumerate(hasil, start=1):
                print(
                    f"{i}. "
                    f"{lagu['judul']} - "
                    f"{lagu['artis']} "
                    f"({format_durasi(lagu['durasi'])})"
                )

        else:
            print("Tidak ada lagu ditemukan.")

    elif pilihan == "4":

        judul_hapus = input(
            "Masukkan judul lagu yang akan dihapus: "
        )

        ditemukan = False

        for lagu in playlist:
            if lagu["judul"].lower() == judul_hapus.lower():
                playlist.remove(lagu)
                ditemukan = True
                print("Lagu berhasil dihapus.")
                break

        if not ditemukan:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":

        if not playlist:
            print("Playlist kosong.")
            continue

        genre_unik = {
            lagu["genre"]
            for lagu in playlist
        }

        lagu_terpanjang = max(
            playlist,
            key=lambda x: x["durasi"]
        )

        lagu_terpendek = min(
            playlist,
            key=lambda x: x["durasi"]
        )

        print("\n======================================")
        print("      STATISTIK PLAYLIST PLAYTUNE")
        print("======================================")

        print(f"Total lagu     : {len(playlist)}")
        print(f"Jumlah genre   : {len(genre_unik)}")
        print(f"Daftar genre   : {genre_unik}")

        print("\nDistribusi genre:")

        for genre in genre_unik:
            jumlah = sum(
                1
                for lagu in playlist
                if lagu["genre"] == genre
            )

            print(f"{genre:<12}: # ({jumlah})")

        print(
            f"\nLagu terpanjang : "
            f"{lagu_terpanjang['judul']} "
            f"({format_durasi(lagu_terpanjang['durasi'])})"
        )

        print(
            f"Lagu terpendek  : "
            f"{lagu_terpendek['judul']} "
            f"({format_durasi(lagu_terpendek['durasi'])})"
        )

        print("======================================")

    elif pilihan == "6":

        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan menu tidak valid.")