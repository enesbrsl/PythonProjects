# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:32:17 2024

"""

sayi=int(input("lütfen bir adet pozitif tamsayı giriniz:"))
toplam=0
sayac=0
gecici=sayi

while(True):
    sayi=sayi/2
    sayac+=1
    if(sayi>0.1 and sayac<=gecici):
        toplam+=sayi
    else:
        break
    
print("toplam={0}".format(toplam))
    
    