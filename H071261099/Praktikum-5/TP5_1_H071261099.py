def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    hasil = ""

    for karakter in teks:
        if karakter.lower() in alfabet:
            hasil += karakter.lower()

    return hasil


def cek_palinrome(teks):
    teks_balik = ''.join(reversed(teks))

    if teks == teks_balik:
        return (True, -1)

    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)

    return (False, -1)


def inti_palinrome(teks):
    teks = bersihkan_teks(teks)

    palindrom_terpanjang = ""
    indeks_awal = 0

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            substring = teks[i:j]

            hasil_cek = cek_palinrome(substring)

            if hasil_cek[0]:
                if len(substring) > len(palindrom_terpanjang):
                    palindrom_terpanjang = substring
                    indeks_awal = i

    return {
        "teks": palindrom_terpanjang,
        "panjang": len(palindrom_terpanjang),
        "indeks_awal": indeks_awal
    }


# Program utama
teks = input("Masukkan teks prasasti: ")

teks_bersih = bersihkan_teks(teks)
hasil = inti_palinrome(teks)

print("Teks Bersih:", teks_bersih)
print("Output Terharap:", hasil)