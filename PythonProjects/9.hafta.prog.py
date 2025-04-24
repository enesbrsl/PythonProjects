class hayvan():
    def __init__(self,ayak,cins):
        self.ayak=ayak
        self.cins=cins
    def konus(self):
        print("ben konusamam.")
# h1=hayvan(2,"bilinmiyor")
# h1.konus()
# print("ayak sayısı=",h1.ayak)
#kopek classına-tureyen class-alt class-sub class denir
class kopek(hayvan):
    def __init__(self,a,c):
        super().__init__(a,c)
    def havla(self):
        super().konus()
        print("havlarım...")

class kus(hayvan):
    def __init__(self,a,c,gaga):
        super.__init__(a,c)
        self.gagauzunlugu=gaga
    def ot(self):
        super().konus()
        print("benim cinsim:",self.cins)
        print("oterım")
        
k1=kopek(4,"fino")
print("ayak sayısı:",k1.ayak)
k1.havla()
kus1=kus(2,"guvercin",2)
kus1.ot()






























    
        
        