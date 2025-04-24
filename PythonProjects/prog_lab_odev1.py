# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:12:46 2024


"""
import math
a=int(input("x^2'li terimin katsayısını giriniz:"))
b=int(input("x'li terimin katsayısını giriniz:"))
c=int(input("sabit terimi giriniz:"))

if(b**2-4*a*c>=0):
    x1=float((-b+math.sqrt(b**2-4*a*c))/(2*a))
    x2=float((-b-math.sqrt(b**2-4*a*c))/(2*a))
    print("Denklemin iki farklı reel kökü vardır:x1 = {0} x2 = {1}".format(x1,x2))
else:
    print("Denklemin reel kökü bulunmamaktadır.")
