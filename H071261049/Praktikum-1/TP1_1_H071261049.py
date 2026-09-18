#detail terkait soal
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]


#jawaban : 
#point 1. hasil dari subtotal untuk kopi, matcha latte dan americano
sub_Kopi = harga[0] * jumlah[0] #hasil = 72000
sub_Matcha_latte = harga[1] * jumlah[1] #hasil = 66000
sub_Americano = harga[2] * jumlah[2] #hasil = 75000

 print(sub_Kopi)
print(sub_Matcha_latte)
print(sub_Americano)


#point 2. hasil terkait total pendapatan
subtotal_pendapatan = [sub_Kopi, sub_Matcha_latte, sub_Americano] #hasil = [72000, 66000, 75000]

print(subtotal_pendapatan)


#point 3. hasil terkait total seluruh pendapatan
total_seluruh = sum(subtotal_pendapatan) # hasil = 213000
BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL #hasil = 198000

print(total_seluruh)
print(pendapatan_bersih)

#point 4. hasil terkait jumlah barang terjual dan target tercapai
jumlah_barang_terjual = jumlah[0] + jumlah[1] + jumlah[2] # hasil = 12
target_tercapai = (total_seluruh > 200000) and (jumlah_barang_terjual > 10) #hasil = True

print(jumlah_barang_terjual)
print(target_tercapai)

