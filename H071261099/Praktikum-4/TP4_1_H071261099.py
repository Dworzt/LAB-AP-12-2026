def hitung_subtotal(harga, jumlah, is_member=False):
    subtotal = harga * jumlah

    if is_member:
        subtotal = subtotal * 0.9

    return subtotal


print("Selamat datang di Kasir Minimarket!")

status_member = input("Apakah Anda member? (y/n): ").lower()
is_member = status_member == "y"

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, is_member)

    print(f"Subtotal {nama_barang}: Rp{subtotal:.0f}")

    total += subtotal

print(f"Total belanja: Rp{total:.0f}")