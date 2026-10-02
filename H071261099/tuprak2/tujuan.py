tujuan= input("masukkan tujuan (pantai/pegunungan/kota): ")
waktu= input("masukkan waktu(pagi/malam): ")
tipe= input("masukkan tipe pengunjung(anak/dewasa): ")

match tujuan:
    case "pantai":
        if waktu=="pagi":
            print("rekomendasi paket: paket A")
    case "pegunungan":
        if waktu=="pagi" and tipe=="dewasa":
            print("paket rekomendasi: paket B")
    case "kota": 
        if waktu=="malam":
            print("rekomendasi paket: paket C") 
    case _:
        print("tidak ada paket yang cocok")  
