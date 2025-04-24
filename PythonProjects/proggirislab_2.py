# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:40:07 2024

@author: ASLI
"""
for i in range(0,10,1):# 0 dan baslar 9 dahıle kadar gıder.10 dahıl degıl
    print(i)
for i in range(0,10):#artıs degerı eger 1 ise artıs mıktarının yazılmasına gerek yoktur
    print(i)#for i in range(10) dıye de yazılabılır.0 dan baslayıp 1 er er artıyorsa eger
#%%


#%%
i=0
while i<10:
    print(i)
    i+=1
#%%
n=int(input("sayı girin:"))
count=0
while n:#burası sıfır olana kadar calısır.bool(0) false dondurur.dıger durumlarda true donere
    count=count+1
    n=n//10
print("baasmak sayısı:",count)
#%%
i=0
toplam=0
while(True):
    print(i+1,end="")
    notu=int(input(".ogrencının notu:"))
    if(100>=notu>=0):
        toplam+=notu
        i+=1
    else:
        break
print("notu gırılen {0} ogrencının not ortalaması={1} ".format(i,toplam/i))
