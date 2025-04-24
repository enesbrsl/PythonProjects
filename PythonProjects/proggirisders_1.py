# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
a=10
print(a)
print(type(a))
#%%
ad="enes"
print(ad)
#yorum satırı # ısaretı ıle acılır
#  '''(uc tırnak) ıle uzun yorum satırına alırız.
# ctrl+1 yorum satırına almanın kısayolu

ad="enes \"adres=bbbbb\""
print(ad)

print("""bugün
        hava
       soguk""")
#  """ ıle kod yazdıgımız formatta cıktı da yazar.yukarıdakı ornektekı gıbı
print("yan\nyana\n mı\n yazar")  
#%%     
a=10
b=5
print(a,"ile",b,"nın carpımı",a*b)
print("%d ile %d nın carpımı %d"%(a,b,a*b))
print("{1} ıle {0} ın carpımı ={2}".format(a,b,a*b))
print(f"{a} ıle {b} nın carpımı={a*b}")
#%%
for i in range(10,110,10):
    # print("%5d"%(i))
    print(f"{i:5}")
#%%
#print("merhaba dunya",end=".")
print("merhaba",end=" ")
print("dunya")
#sep seperate
print("bugun","hava","guzel",sep="-")
#her bır strıngı ıcınde yazan seyle ayırır.
print(*"dunya",sep=".")
print(*"dunya",sep="\n")
#%% input external data
while(1):
        try:
            vize=int(input("vize="))
            final=int(input("final="))
            bolum=a/b
        except:
             print("lutfen rakam girin:")
        else:
             ort=vize*0.4+final*0.6
             print(f"ortalama={ort}")
        break
        


           
           
           



