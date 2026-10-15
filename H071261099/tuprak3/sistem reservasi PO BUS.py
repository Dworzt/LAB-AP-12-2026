while True:
    try:
        N= int(input("masukkan maksimal kursi bus: "))
        if N <=0:
            print("jumlah kursi harus lebih dari nol!")
        else:
            break
    except ValueError:
        print("input jumlah kursi harus berapa angka")
sisa_kursi= N
total_pendapatan=0
print("\n--sistem reservasi PO BUS dimulai---")
while sisa_kursi>0:
    print(f"\n sisa kursi:{sisa_kursi}")
    try:
        umur= int(input("masukkan umur penumpang:"))
        if umur<0:
            print("umur tidak valid!")
            continue
        if umur <=5:
            kategori="balita"
            harga=0
        elif umur<=12:
            kategori="anak"
            harga=50000
        else:
            kategori="dewasa"
            harga=100000
        print(f"kategori:{kategori}-harga:rp{harga:,}".replace(",","."))
        total_pendapatan+=harga
        sisa_kursi-=1
    except ValueError:
        print("input umur harus berupa angka!") 
        continue
print("\n---semua kursi terisi")
print(f"total pendapatan perjalanan PO BUS kali ini: Rp{total_pendapatan}")