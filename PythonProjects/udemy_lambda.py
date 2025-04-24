liste1=[1,2,3,4,5]
liste2=[i*2 for i in liste1]
print(liste2)
print("*"*80)
def ikiylecarp(x):
    return x*2
print(ikiylecarp(3))


ikiylecarp=lambda x:x*2
print(ikiylecarp(3))
print("*"*80)
def toplam(x,y,z):
    return x+y+z
print(toplam(3,45,4))

toplama=lambda x,y,z:x+y+z
print(toplam(3,45,4))
print("*"*80)

def terscevir(s):
    return s[::-1]
print(terscevir("python programlama"))

terscevir=lambda s:s[::-1]
print(terscevir("python programlama"))
#%% asal sayı bulma
def asalmi(sayı):
    if(sayı==1):
        return False
    elif(sayı==2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı%i==0):
                return False
        return True
    
while(True):
    sayı=input("bir sayı giriniz:")
    if(sayı == "q"):
        break
    else:
        sayı=int(sayı)
        if(asalmi(sayı)):
            print(sayı,"asal sayıdır.")
        else:
            print(sayı,"asal sayı degildir.")
#%% sayının tam bolenlerini bulma

def tambolen(sayı):
    liste=[]
    for i in range(2,sayı):
        if(sayı%i==0):
            liste.append(i)
    return liste

while(True):
    sayı=input("bir sayı giriniz(cıkmak ıcın q'ya basın):")
    if(sayı=="q"):
        print("program sonlandırılıyor.")
        break
    else:
        sayı=int(sayı)
        print(tambolen(sayı))
#%%



           
    
    

    
       


























