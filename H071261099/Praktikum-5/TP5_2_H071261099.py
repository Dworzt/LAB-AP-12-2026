def cek_kata(teks, kata):
    indeks = []
    start = 0

    teks_kecil = teks.lower()
    kata_kecil = kata.lower()

    while True:
        posisi = teks_kecil.find(kata_kecil, start)

        if posisi == -1:
            break

        indeks.append(posisi)
        start = posisi + 1

    return indeks


def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    # Cek karakter sebelum kata
    if i > 0:
        sebelum = teks[i - 1].lower()

        if sebelum in alfabet:
            return False

    # Cek karakter setelah kata
    posisi_akhir = i + panjang

    if posisi_akhir < len(teks):
        sesudah = teks[posisi_akhir].lower()

        if sesudah in alfabet:
            return False

    return True


def sensor_kata(teks, kata, simbol):
    indeks_kemunculan = cek_kata(teks, kata)

    indeks_valid = []

    for indeks in indeks_kemunculan:
        if cek_batas_kata(teks, indeks, len(kata)):
            indeks_valid.append(indeks)

    hasil = ""
    i = 0

    while i < len(teks):
        if i in indeks_valid:
            hasil += simbol * len(kata)
            i += len(kata)
        else:
            hasil += teks[i]
            i += 1

    return hasil, len(indeks_valid), indeks_valid


# Program utama
teks = input("Masukkan teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)

print("Hasil Sensor:", hasil)
print("Jumlah:", jumlah)
print("Indeks:", indeks)