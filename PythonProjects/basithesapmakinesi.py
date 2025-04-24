# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:45:50 2024

@author: ASLI
"""

print("""***********************
      HESAP MAKİNESİ
      
      1.toplama ıslemı
      2.cıkarma ıslemı
      3.carpma ıslemı
      4.bolme ıslemı
           
      
************************
""")
a=int(input("birinci sayi:"))
b=int(input("ıkıncı sayi:"))
islem=input("islem giriniz:")

if(islem=="1"):
    print("{} ile {} in toplamı {} dır".format(a,b,a+b))
elif(islem=="2"):
    print("{} ile {} in farkı {} dır".format(a,b,a-b))
elif(islem=="3"):
    print("{} ile {} in carpımı {} dır".format(a,b,a*b))
elif(islem=="4"):
    print("{} ile {} in bolumu {} dır".format(a,b,a/b))
else:
    print("gecersiz islem.......")