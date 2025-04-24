#%% parola girme
parola=input("lütfen parolanızı girin:")
tr_karakterler="şçöğüİıÖÜ"
for i in parola:
    if(i in tr_karakterler):
        print("turkce karakter giremezsiniz.")
        break
    
#%% stringdeki farklı karakterleri bulma
metin1="enesali"
metin2="bursalı"
for i in metin1:
    if (not  i in metin2):
        print(i,end=" ")
        
#%% faktoriyel hesaplama
sayı=int(input("sayı :"))
faktoriyel=1
if(sayı<0):
    sayı=abs(sayı)
for i in range(1,sayı+1):
    faktoriyel*=i
print(faktoriyel)
#%% palindrom kelime bulma

while(True):
    kelime=input("kelime:")
    uzunluk=len(kelime)
    durum="palindrom"
    for k in kelime:
        if(k!=kelime[uzunluk-1]):
            durum="palindrom degil"
            break
        uzunluk-=1
    print(kelime,"kelimesi",durum)
#%% 2.yöntem
kelime=input("kelime girin:")
ters_kelime=kelime[::-1]
if kelime==ters_kelime :
    print(kelime,"palindrom")
else:
    print(kelime,"palindrom degıl")
#%% stringin tersini bulma
kelime=input("kelime girin:")
ters_kelime=""
for i in range(len(kelime)-1,-1,-1):
    ters_kelime+=kelime[i]
print(ters_kelime)  
#%% carpım tablosu ornegi
olcu=int(input("carpım tablosu olcusu girin:"))
for satir in range(1,olcu+1):
    for sutun in range(1,olcu+1):
        print("{0:4}".format(satir*sutun),end=" ")
    print()

    
  
        

























#%% basamak sayısı bulma
sayı=int(input("bir sayı girin:"))
count=0
while sayı:
    count+=1
    sayı=sayı//10
print("basamak:",count)
#%%

