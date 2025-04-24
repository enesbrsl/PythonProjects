
#%%
a="enes"
print(a)
print(type(a))
# yorum satırına alır
ad="enes\"adres=bbb\""
print(ad)
ad="enes'adres=bbb'"
#%%
print("""salih
odada
uyuyor""")
print(""" bugun     hava      
      sıcak""")
print( "yan \nyana \n mı yazar")
#%%
a=5
b=3
print(a,"ile",b,"nin carpımı",a*b)
print(a,"nın",b,"ye bolumu",a/b)
print("%d ile %d nin carpımı %d"%(a,b,a*b))#c dili ile benzer
print("{1} ile {0} nın carpımı {2}".format(a,b,a*b))
print(f"{a} ile {b} nın carpımı {a*b}")