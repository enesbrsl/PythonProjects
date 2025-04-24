bool()
bool(0)
bool("")
bool(0.0)
bool(1.2)
bool( )
bool(" ")
parola="python"
girdi=input("parolayı giriniz:")
if(girdi.lower()==parola):#buyukharf girildıgı zaman da parolayı dogru kabul eder.buyuk kucuk harf duyarlılıgı vardır.
    print("basarıyla giris yapıldı.")
#%%
x=10
y=10
if(x<y):
    print("%s<%s"%(x,y))
elif(x>y):
    print("%s>%s"%(x,y))
else:
    print("%s=%s"%(x,y))
#%%
def kökal(sayi):
    if(sayi<0):
        print("lütfen pozitif sayı giriniz")
        return
    sonuc=sayi**0.5
    print("sonuc:",sonuc)
    
kökal(-144)
kökal(64)
#%%
def ask_ok():
    ok=input("cıkmak ıstedıgınıze emın mısınız?")
    if(ok in ("y","ye","yes")):
        print("basarıyla cıkıs yapıldı.")
    else:
        print("cıkıs yapılmadı.")

ask_ok()
#%%
import random
tutulan=random.randrange(0,10)
girdi=int(input("bir sayi giriniz:"))
print("tutulan sayi:",tutulan)
if(girdi==tutulan):
    print("dogru bıldınız")
elif(girdi<tutulan):
    print("daha buyuk sayi  girin")
else:
    print("daha kucuk sayi giriniz")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    