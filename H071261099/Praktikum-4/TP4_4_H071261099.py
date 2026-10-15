def konversi_suhu(suhu, asal, tujuan):
    skala = ["C", "F", "K"]

    if asal not in skala or tujuan not in skala:
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == tujuan:
        return suhu

    if asal == "C" and tujuan == "F":
        return (suhu * 9/5) + 32
    elif asal == "C" and tujuan == "K":
        return suhu + 273.15
    elif asal == "F" and tujuan == "C":
        return (suhu - 32) * 5/9
    elif asal == "F" and tujuan == "K":
        return (suhu - 32) * 5/9 + 273.15
    elif asal == "K" and tujuan == "C":
        return suhu - 273.15
    elif asal == "K" and tujuan == "F":
        return (suhu - 273.15) * 9/5 + 32


print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)

        asal = input("Skala asal (C/F/K): ").upper()
        tujuan = input("Skala tujuan (C/F/K): ").upper()

        hasil = konversi_suhu(suhu, asal, tujuan)

        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")

    except ValueError:
        print("Error: Skala suhu tidak dikenali.")