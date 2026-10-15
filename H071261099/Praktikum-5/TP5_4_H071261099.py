def deteksi_anomali_email(email):
    error = []

    # Aturan 1: harus memiliki tepat satu @
    if email.count("@") != 1:
        error.append("Harus memiliki tepat satu karakter @.")
        return error

    bagian = email.split("@")
    local = bagian[0]
    domain = bagian[1]

    # Aturan 2: local dan domain tidak boleh kosong
    if local == "" or domain == "":
        error.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    # Aturan 3: tidak boleh ada spasi
    if " " in email:
        error.append("Email tidak boleh mengandung spasi.")

    # Aturan 4: aturan bagian local
    if local != "":
        if local[0] == "." or local[-1] == ".":
            error.append("Bagian local tidak boleh diawali atau diakhiri titik.")

        if ".." in local:
            error.append("Bagian local tidak boleh mengandung titik berurutan.")

    # Aturan 5: aturan bagian domain
    if domain != "":
        if "." not in domain:
            error.append("Bagian domain wajib memiliki minimal satu titik.")

        if ".." in domain:
            error.append("Bagian domain tidak boleh mengandung titik berurutan.")

        if domain[-1] == ".":
            error.append("Bagian domain tidak boleh diakhiri titik.")

        if not (
            domain.endswith(".com")
            or domain.endswith(".id")
            or domain.endswith(".ac.id")
        ):
            error.append("Wajib berakhiran dengan .com, .id, atau .ac.id.")

    return error


def cetak_daftar(daftar_email_valid, karakter_border):
    if len(daftar_email_valid) == 0:
        print("Tidak ada email valid.")
        return

    panjang_maksimal = len(max(daftar_email_valid, key=len))

    lebar = panjang_maksimal + 2

    border = karakter_border * (lebar + 2)

    print("\n--- HASIL EMAIL VALID ---")
    print(border)

    for email in daftar_email_valid:
        print(karakter_border + " " + email.ljust(lebar) + karakter_border)

    print(border)


# Program utama
daftar_email_valid = []

print("=== Sistem Pencatatan Email Valid ===")

karakter_border = input("Masukkan border dengan karakter bebas: ")

while True:
    email = input("\nMasukkan email: ")

    if email.lower() == "tutup":
        break

    error = deteksi_anomali_email(email)

    # Cek duplikat
    if len(error) == 0:
        if email in daftar_email_valid:
            error.append("Email sudah terdaftar (Duplikat).")

    if len(error) == 0:
        daftar_email_valid.append(email)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")

        for alasan in error:
            print("-", alasan)

cetak_daftar(daftar_email_valid, karakter_border)