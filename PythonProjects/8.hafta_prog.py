class Nokta:
    #contructor (kurucu) metod
    def __init__(self,a=0,b=0):
        self.x=a #attribute
        self.y=b
        self.__hidden=5 #encapsulation (private variable)
    def noktalari_yaz(self,objectname):
        print(objectname,"(x,y)=(",self.x,",",self.y,")")
          
    def gizli_attribute_yaz(self):
        print("__hidden=",self.__hidden)
p1=Nokta()
# print(p1.__hidden)#hata
print(p1.x)
#%%
class Personel:
    def __init__(self,name="",surname="",maas=0):
        self.name=name
        self.surname=surname
        self.maas=maas
    def personel_bilgisi_yaz(self):
        print("%s %s personelinin maaşı=%d TL"%(self.name,self.surname,self.maas))

p1=Personel("ahmet","nsbfhs",5000)
p1.personel_bilgisi_yaz()

p2=p1 #shallow copy
p1.name="mehmet"
p1.personel_bilgisi_yaz()
print(p1==p2)
import copy
p3=copy.deepcopy(p1)
p3.name="ayse"
p3.personel_bilgisi_yaz()
p1.personel_bilgisi_yaz()
print(p1==p3)



















