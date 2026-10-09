jawaban = input("masukkan nomor soal yang akan dijalankan: ")
try:
    if "1" in jawaban:
        def bersihkan_teks(teks):
            alfabet = "abcdefghijklmnopqrstuvwxyz"
            hasil = ""
            for char in teks.lower():
                if char in alfabet:
                    hasil += char
            return hasil

        def cek_palinrome(teks):
            teks_dibalik = "".join(reversed(teks))
            if teks == teks_dibalik:
                return (True, -1)
    
    
            for i in range(len(teks)):
                if teks[i] != teks_dibalik[i]:
                    return (False, i)

        def inti_palinrome(teks):
            teks_bersih = bersihkan_teks(teks)
            n = len(teks_bersih)
    
            palindrom_terpanjang = ""
            indeks_awal = -1
            panjang_maks = 0
            
            for i in range(n):
                for j in range(i + 1, n + 1):
                    hasil_bersih = teks_bersih[i:j]
                    is_palin, _ = cek_palinrome(hasil_bersih)
            
                    if is_palin:
                        if len(hasil_bersih) > panjang_maks:
                            panjang_maks = len(hasil_bersih)
                            palindrom_terpanjang = hasil_bersih
                            indeks_awal = i
            output = panjang_maks, palindrom_terpanjang, indeks_awal
            print (input_teks)
            print ("Teks Bersih:", teks_bersih) 
            print (f"Output Terharap: ('teks': {panjang_maks}, 'panjang': {palindrom_terpanjang}, 'indeks awal': {indeks_awal})")  
             
            return {
                    "teks": palindrom_terpanjang,
                    "panjang": panjang_maks,
                    "indeks awal": indeks_awal
                }


        input_teks = input("Masukkan teks prasasti: ")
        if "" in input_teks:
            hasil = inti_palinrome(input_teks)
        
        
except ValueError:
    print ("nomor soal tidak sesuai input.")        