#%%
class calisan():
    def __init__(self,isim="",maas=0,departman=""):
        print("init fonksiyonu calıstı....")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileri_göster(self):
        print("isim:{}\nmaas:{}\ndepartman:{}".format(self.isim,self.maas,self.departman))
        
    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman
class yönetici(calisan):
    pass
yönetici1=yönetici("enes",5000,"yazılım")
yönetici1.bilgileri_göster()
yönetici1.departman_degistir("insan kaynakları")
print("-----------------------------")
yönetici1.bilgileri_göster()
calisan1=calisan("enes",3000,"teknik destek")
print("-----------------------------")
calisan1.bilgileri_göster()
print("-----------------------------")
dir(yönetici())
class yönetici(calisan):
    def zam_yap(self,zam_miktari):
        self.maas+=zam_miktari
yönetici2=yönetici("mustafa",3000,"siber güvenlik")
yönetici2.zam_yap(1000)
yönetici2.bilgileri_göster()
#%% override metodu-miras alınan degil kendi metodunu kullanır.
class yönetici(calisan):
    def __init__(self,isim,maas,departman,kisisayisi):
        print("yönetici sinifinin init fonk calisti")
        
        self.isim=isim
        self.maas=maas
        self.departman=departman
        self.kisisayisi=kisisayisi
    def bilgileri_göster(self):
        print("yönetici sınıfının özellikleri\nisim:{}\nmaas:{}\ndepartman:{}\nkisi sayısı:{}".format(self.isim,self.maas,self.departman,self.kisisayisi))
yönetici1=yönetici("kerem",8000,"yapay zeka",10)
yönetici1.bilgileri_göster()
#%% super kullanımı
class calisan():
    def __init__(self,isim,maas,departman):
        print("calısan sinifinin init fonk.")
        self.isim=isim
        self.maas=maas
        self.departman=departman
    def bilgileri_göster(self):
        print("calisan bilgileri:\nisim:{}\nmaas:{}\ndepartman:{}".format(self.isim,self.maas,self.departman))
        
class yönetici(calisan):
    def __init__(self,isim,maas,departman,kisisayisi):
        super().__init__(isim,maas,departman)
        print("yönetici sinifinin init fonk. calisti")
        self.kisisayisi=kisisayisi
        
    
        
        













































