#%%
while(True):
    try:
        a=int(input("bölünen giriniz:"))
        b=int(input("bölen giriniz:"))
        print(a/b)
        break
    except ZeroDivisionError:
        print("böleni sıfır girmeyin.")
    except ValueError:
        print("lütfen sayi girin")
    except:
        print("bilinmeyen hata olustu")

    

#%%
tup=('a','b','c','d')
try:
    tup[2]='c'
except TypeError:
    print("tupple degistirilemez")

#%%
try: 
    a = [10,20,30]
    index=int(input("Kaçıcı Eleman:"))
    print (a[index])
except IndexError:
    print("Indeks Hatası oluştu")
#%% FileNotFoundError


filename="myfile2.txt"
try:
    file=open(filename,"r")
    notu=int(file.readline())#geriye string dondurur
    print(notu)
except FileNotFoundError:
    print(f"{filename} dosyası bulunamadı")
except ValueError as err:
    errmsg=err.args
    print(errmsg)
#%% inheritance(kalıtım) polymorphizm(cok bicimlilik) encapsolation(kapsülleme) 
class Nokta:
    def __init__(self,a,b):
        self.x=a
        self.y=b
object1=Nokta(20,30)
object2=Nokta(50,100)
print(object1.x)
print(object1.y)
print(object2.x)
print(object2.y)
# print(type(Nokta))
# print(type(object1))
