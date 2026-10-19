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

    if hasil:
        print(f"\nDitemukan {len(hasil)} buku:")
        for i, buku in enumerate(hasil, start=1):
            print(
                f"{i}. {buku['judul']} | "
                f"{buku['penulis']} | "
                f"Rp{buku['harga']} | "
                f"Stok: {buku['stok']}"
            )
    else:
        print("Tidak ada buku yang ditemukan.")


def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():

            stok_baru = buku["stok"] + jumlah

            if stok_baru < 0:
                print("Gagal! Stok tidak boleh negatif.")
                return

            buku["stok"] = stok_baru

            print(
                f"Stok buku '{buku['judul']}' berhasil diperbarui. "
                f"Stok sekarang: {buku['stok']}"
            )
            return

    print("Buku tidak ditemukan.")


def ringkasan_inventaris(inventaris):
    if not inventaris:
        print("Inventaris kosong.")
        return

    jumlah_buku = len(inventaris)

    total_stok = sum(
        buku["stok"]
        for buku in inventaris
    )

    total_aset = sum(
        buku["harga"] * buku["stok"]
        for buku in inventaris
    )

    buku_termahal = max(
        inventaris,
        key=lambda buku: buku["harga"]
    )

    print("\n===== RINGKASAN INVENTARIS =====")
    print(f"Jumlah jenis buku : {jumlah_buku}")
    print(f"Total stok buku   : {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(
        f"Buku termahal     : "
        f"{buku_termahal['judul']} "
        f"(Rp{buku_termahal['harga']})"
    )


inventaris = []

while True:
    print("\n===== BOOKNEST =====")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan nama penulis: ")

        try:
            harga = int(input("Masukkan harga buku: "))
            stok = int(input("Masukkan stok awal: "))

            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif.")
                continue

            tambah_buku(
                inventaris,
                judul,
                penulis,
                harga,
                stok
            )

        except ValueError:
            print("Input harga dan stok harus berupa angka.")

    elif pilihan == "2":
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)

    elif pilihan == "3":
        judul = input("Masukkan judul buku: ")

        try:
            perubahan = int(
                input(
                    "Masukkan jumlah perubahan stok "
                    "(+ tambah, - kurangi): "
                )
            )

            update_stok(
                inventaris,
                judul,
                perubahan
            )

        except ValueError:
            print("Jumlah perubahan harus berupa angka.")

    elif pilihan == "4":
        ringkasan_inventaris(inventaris)

    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest.")
        break

    else:
        print("Pilihan menu tidak valid.")
        continue