# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 01:20:50 2024


"""

sayi=int(input("lütfen bir sayi giriniz:"))
ciftsayac=0
teksayac=0
cifttop=0
tektop=0

for i in str(sayi):
    i=int(i)
    if(i%2==0):
        cifttop+=i
        ciftsayac+=1
    else:
        tektop+=i
        teksayac+=1
print("girilen sayıda {0} çift rakam ve {1} tek rakam bulunmaktadır.".format(ciftsayac,teksayac))
print("çift rakamların toplamı:{0}\ntek rakamların toplamı:{1}".format(cifttop,tektop))
        
        