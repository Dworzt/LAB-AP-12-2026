menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
sub_kopi = jumlah[0] * harga[0]
sub_matcha = jumlah[1] * harga[1]
sub_americano = jumlah[2] * harga[2]
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]
total_seluruh = sum(subtotal_pendapatan)
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL
jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10
print (subtotal_pendapatan)
print (pendapatan_bersih)
print (target_tercapai)
