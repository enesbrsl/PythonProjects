# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:03:22 2024

@author: ASLI
"""
print("""*************************
       KULLANICI GİRİŞİ
*************************""")
kullanici_adi="enes"
parola=12345

kullaniciadi=input("kullanici adi:")
parolaa=int(input("parola:"))

if(kullanici_adi==kullaniciadi and parola!=parolaa):
    print("parola hatali......")
elif(kullanici_adi!=kullaniciadi and parola==parolaa):
    print("kullanici adi hatali.....")
elif(kullanici_adi!=kullaniciadi and parola!=parolaa):
    print("parola ve kullanıcı adı hatalı......")
else:
    print("sisteme basrıyla giris yapıldı...")
