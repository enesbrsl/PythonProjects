import random
import time
print("sayı tahmin oyunu")
tahmin_hakki=7
rastgele_sayi=random.randint(1, 40)
while(True):
    tahmin=int(input("1 ile 40 arasinda bir sayi girin:"))
    if(tahmin<rastgele_sayi):
        print("sonuc yazdiriliyor...")
        time.sleep(1)
        print("daha buyuk bir sayi girin")
        tahmin_hakki-=1
    elif(tahmin>rastgele_sayi):
        print("sonuc yazdiriliyor...")
        time.sleep(1)
        print("daha kucuk bir sayi girin")
        tahmin_hakki-=1
    else:
        print("sonuc yazdiriliyor...")
        time.sleep(1)# 1 saniye beklemeye yarayan fonksiyondur
        print("tebrikler!sayimiz:",rastgele_sayi)
        break
    if(tahmin_hakki==0):
        break
        
        