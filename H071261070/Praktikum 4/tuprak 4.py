# soal 1 kaasir minimarket
print("Selamat datang di Kasir Minimarket!")

def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal = subtotal * 90 / 100

    return subtotal


status_member = input("Apakah Anda member? (y/n): ")

if status_member == "y":
    adalah_member = True
else:
    adalah_member = False

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, adalah_member)

    print("Subtotal " + nama_barang + ": Rp" + str(int(subtotal)))

    total = total + subtotal

print("Total belanja: Rp" + str(int(total)))


#soal 2 Rekap Nilai Siswa
def rekap_nilai(*args):
    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return rata_rata, nilai_tertinggi, nilai_terendah


nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")

    if input_nilai == "":
        break

    nilai.append(float(input_nilai))


if len(nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata_rata, nilai_tertinggi, nilai_terendah = rekap_nilai(*nilai)

    print("Rata-rata kelas:", rata_rata)
    print("Nilai tertinggi:", int(nilai_tertinggi))
    print("Nilai terendah:", int(nilai_terendah))


# soal 3 Hitung Mundur Roket
def hitung_mundur(angka):
    print(angka)

    if angka == 0:
        print("Luncurkan!")
    else:
        hitung_mundur(angka - 1)


while True:
    angka_awal = int(input("Masukkan angka awal hitung mundur: "))

    if angka_awal < 0:
        print("Input tidak valid, angka tidak boleh negatif.")
    else:
        break


hitung_mundur(angka_awal)


#soal 4 konversi suhu
def konversi_suhu(suhu, asal, tujuan):
    if asal not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if tujuan not in ["C", "F", "K"]:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == "C" and tujuan == "F":
        hasil = (suhu * 9 / 5) + 32
    elif asal == "C" and tujuan == "K":
        hasil = suhu + 273.15
    elif asal == "F" and tujuan == "C":
        hasil = (suhu - 32) * 5 / 9
    elif asal == "F" and tujuan == "K":
        hasil = (suhu - 32) * 5 / 9 + 273.15
    elif asal == "K" and tujuan == "C":
        hasil = suhu - 273.15
    elif asal == "K" and tujuan == "F":
        hasil = (suhu - 273.15) * 9 / 5 + 32
    else:
        hasil = suhu

    return hasil


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu == "selesai":
        break

    try:
        suhu = float(input_suhu)

        asal = input("Skala asal (C/F/K): ")
        tujuan = input("Skala tujuan (C/F/K): ")

        hasil = konversi_suhu(suhu, asal, tujuan)

        print("Hasil:", suhu, asal, "=", hasil, tujuan)

    except ValueError:
        print("Error: Skala suhu tidak dikenali.")