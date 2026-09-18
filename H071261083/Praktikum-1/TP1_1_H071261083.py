menu = ["kopi_susu", "matcha_latte", "americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

print ("Laporan Penjualan Kopi Senja")

subtotal_kopi = harga[0] * jumlah[0]
subtotal_matcha = harga[1] * jumlah [1]
subtotal_americano = harga[2] * jumlah[2]
print (f"subtotal kopi susu : Rp {subtotal_kopi}")
print (f"subtotal matcha latte : Rp {subtotal_matcha}")
print (f"subtotal americano : Rp {subtotal_americano}")

subtotal_pendapatan = subtotal_kopi + subtotal_matcha + subtotal_americano
print (f"subtotal pendapatan : Rp {subtotal_pendapatan}")

biaya_operasional = 15000
pendapatan_bersih = subtotal_pendapatan - biaya_operasional
print (f"pendapatan bersih : Rp {pendapatan_bersih}")

jumlah_barang = jumlah[0] + jumlah [1] + jumlah[2]
target_tercapai = subtotal_pendapatan > 200000 and jumlah_barang > 10
print (f"target tercapai : {target_tercapai}")