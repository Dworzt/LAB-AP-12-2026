print("=== rekapitulasi transaksi dins store===")
print("ketik '0' untuk menutup toko dan mengakhiri sesi.")
while True:
    try:
        jumlah= int(input("\n masukkan jumlah item:"))
        if jumlah == 0:
            print("toko ditutup. sesi rekap selesai.")
            break
        if jumlah < 0:
            print("jumlah tidak boleh negatif")
            continue
        if jumlah > 100:
            print("maksimal 100 item per transaksi")
            continue
        print(f"transaksi (jumlah)item berhasil")
    except ValueError:
        print("input harus berupa angka")