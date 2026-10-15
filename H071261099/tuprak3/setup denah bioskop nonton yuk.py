print("===setup denah bioskop nonton yuk===")
while True:
    try:
        n=int(input("masukkan jumlah baris:"))
        if n <= 0:
            print("jumlah baris harus lebih dari 0!")
            continue
        m=int(input("masukkan jumlah kuris per baris:"))
        if m<= 0:
            print("jumlah kursi haris lebih dari 0!")
            continue
        break
    except ValueError:
        print("input baris harus berupa angka!")
        print("\n===daftar kursi tersedia===")
for baris in range(1,n+1):
    for kursi in range(1,m+1):
        if kursi==13:
            continue
        if baris==1 and kursi %2==0:
            continue
        print(f"baris{baris}-kursi{kursi}")
        