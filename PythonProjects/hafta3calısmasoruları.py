#%% isim yazdırma
isim=input("isim=")
sayi=int(input("kac defa tekrarlansin="))
for i in range(sayi):
    print(isim)
#%% cift sayıların toplamı
sayi1=int(input("sayı girin:"))
sayi2=int(input("sayı girin:"))
if(sayi1<sayi2):
    cifttop=0
    for i in range(sayi2-sayi1-1):
        sayi1+=1
        if(sayi1%2==0):
            cifttop+=sayi1
elif(sayi1==sayi2):
    print("lutfen farklı sayılar girin...")
else:
    cifttop=0
    for i in range(sayi1-sayi2-1):
        sayi2+=1
        if(sayi2%2==0):
            cifttop+=sayi2
    
      
print("cifttoplam:",cifttop)       
#%% asal sayı bulma
sayi=int(input("sayı girin:"))
kontrol=0
for i in range(2,sayi):
    if(sayi==2):
         kontrol=1
         break
    elif(sayi%i!=0):
       kontrol=1
   
    elif(sayi%i==0):
        kontrol=0
        break
if(kontrol==1):
    print("asal sayı")

else:
    print("asal sayı degil")
#%% 5 e bolunen sayıların toplamını bulma
sayi1=int(input("sayı girin:"))
sayi2=int(input("sayı girin:"))
if(sayi1<sayi2):
    cifttop=0
    for i in range(sayi2-sayi1-1):
        sayi1+=1
        if(sayi1%5==0):
            cifttop+=sayi1
elif(sayi1==sayi2):
    print("lutfen farklı sayılar girin...")
else:
    cifttop=0
    for i in range(sayi1-sayi2-1):
        sayi2+=1
        if(sayi2%5==0):
            cifttop+=sayi2
            
print("cifttoplam:",cifttop)
#%% ortalma hesaplama
top=0
adet=0
while(True):
    sayi=input("sayı girin(programdan cıkmak ıcın q ya basın)=")
    if(sayi=="q"):
        print("programdan cıkılıyor...")
        break
    else:
        sayi=int(sayi)
        top+=sayi
        adet+=1
print("ortalama=",top/adet)
#%% tek-cıft sayıları bulma

sayi=[]
for i in range(10):
    i=int(input("sayı girin:"))
    sayi.append(i)
cifttop=0
tektop=0
tekad=0
ciftad=0
for i in sayi:
    if(i%2==0):
        cifttop+=i
        tekad+=1
    else:
        tektop+=i
        ciftad+=1
print("teklerin ortalamsı:",tektop/tekad)
print("cıftlerin ortalamsı:",cifttop/ciftad)
#%% obeb okek hesaplama
sayi1=int(input("1.sayıyı girin:"))
sayi2=int(input("2.sayıyı girin:"))































        

    

    
        
       