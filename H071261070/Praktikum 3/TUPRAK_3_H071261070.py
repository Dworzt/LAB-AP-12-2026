# #REKAPITULASI TRANSAKSI "DINS STORE"
# print("--- Reakpitulasi Transaksi DIns Store")
# print("Ketik '0' untuk menutup toko dan mengakiri sesi.")


# while True:
#     try: 
#         item = int(input("Masukkan jumlah item: "))
#         if item == 0:
#             break
#         elif item < 0:
#             print("Jumlah tidak boleh negatif")
#             print()
#         elif item > 0 and item <= 100:
#             print(f"Transaksi {item} item berhasil!")
#             print()
#         elif item > 100:
#             print("Maksimal 100 per transakasi!")
#             print()
#     except:
#         print("Input harus berupa angka!")
#         print()
# print("Toko ditutup, Sesi rekap selesai.")


# #DENAH KURSI BIOSKOP
# print("--- Setup Denah Bioskop NontonYuk ---")

# while True:
#     try:
#         baris = int(input("Masukkan jumlah baris: "))
#         if baris <= 0:
#             print("Jumlah baris harus lebih dari 0!")
#             continue
#         kursi = int(input("Masukkan jumlah kursi per baris: "))
#         if kursi <= 0:
#             print("Jumlah kursi tidak boleh 0")
#             continue
#         break
#     except:
#         print("Input baris harus berupa angka!")

# for a in range(1, baris + 1):
#     for b in range(1, kursi + 1):
#         if b == 13:
#             continue
#         if a == 1 and b % 2 == 0:
#             continue
#         print(f"Baris {a}, Kursi {b}")


#SISTEM RESERVASI PO BUS
pendapatan = 0
while True:
    try:
        maksimal_kursi = int(input("Masukkan maksimal kursi: "))
        while maksimal_kursi < 0:
            print("Input tidak boleh kurang dari 1")
            maksimal_kursi = int(input("Masukkan maksimal kursi: "))
        while maksimal_kursi > 0:
            try: 
                print()
                print("--- Sistem Revervasi PO BUS Dimulai ---")
                print()
                print(f"Sisa kursi: {maksimal_kursi}")
                umur_penumpang = int(input("Masukkan umur penumpang: "))
                if 0 <= umur_penumpang <= 5:
                    ticket = 0
                    kategori = "Balita - Tiket Gratis (Rp 0)"
                elif 6 <= umur_penumpang <= 12:
                    ticket = 50000
                    kategori = "Anak - Harga: Rp 50.000"
                elif umur_penumpang > 12:
                    ticket = 100000
                    kategori = "Dewasa - Harga: Rp 100.000"
                else:
                    "Umur tidak valid"
                    continue
                maksimal_kursi -= 1
                pendapatan += ticket
                print(f"Kategori: {kategori}")
            except:
                print("Input harus berupa angka!")
                print()
        print()
        print("--- Semua Kursi Terisi ---")
        print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {pendapatan}")
        break
    except:
        print("Input harus berupa angka!")


