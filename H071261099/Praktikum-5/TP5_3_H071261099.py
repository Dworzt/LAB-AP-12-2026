ALFABET = "abcdefghijklmnopqrstuvwxyz"


def cek_sandi(ch, k):
    if ch.lower() not in ALFABET:
        return ch

    huruf_kecil = ch.lower()

    posisi = ALFABET.find(huruf_kecil)

    posisi_baru = (posisi + k) % 26

    hasil = ALFABET[posisi_baru]

    if ch.isupper():
        return hasil.upper()
    else:
        return hasil


def mesin_enkripsi(teks, k):
    hasil = ""

    for ch in teks:
        hasil += cek_sandi(ch, k)

    return hasil


def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)


def retas_sandi(sandi, kata_kunci):
    hasil = []

    for kunci in range(26):
        pesan_asli = mesin_dekripsi(sandi, kunci)

        if pesan_asli.lower().find(kata_kunci.lower()) != -1:
            hasil.append((kunci, pesan_asli))

    return hasil


# Program utama
sandi = input("Masukkan pesan tersandi: ")
kata_kunci = input("Masukkan kata kunci target: ")

hasil = retas_sandi(sandi, kata_kunci)

print("Hasil:", hasil)