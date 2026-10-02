jarak= float(input("masukkan jarak(km): "))
express= input("masukkan layanan express(ya/tidak): ")
if jarak <5:
    tarif= 10000
elif jarak <=20:
    tarif= 20000
else:
    tarif= 35000
tambahan= 15000 if express== "ya" else 0
total = tarif+tambahan
print("total tarif pengiriman: rp", total)