name="istanbul"#string ummutable-degısmezdir
name[0]="i"
print(name)
#%%reference type and shallowcopy-sığ kopyalama
cities=["samsun",34,"ordu",52,"anakara",6]
newcities=cities
print("id cities",id(cities))
print("id newcities",id( newcities))# ikisinin de adersi aynıdır.aynı adresi kullanır.
newcities[1]=55
print("cities=",cities)
print("newcities=",newcities)
#---------shallow copy
#newcitiesshallow=cities[:]#method-1 for shallow copy
import copy
newcitiesshallow=copy.copy(cities)#method-2 for shallow copy

print("id cities",id(cities))
print("id newcities",id( newcitiesshallow))
print("-"*40)

newcitiesshallow[4]="sinop"
print("cities=",cities)#citiesde degisiklik olmaz
print("newcities=",newcitiesshallow)








#%%
def double(liste):
    for index,value in enumerate(liste):
        liste[index]=value**2
        
numberlist=[2,4,6,8]
print("fonk cagırmadan once numberlist:",numberlist)
#double(numberlist)
double(numberlist[:])#shallow copy
print("fonk cagırdıktan sonra numberlist:",numberlist)

#%% shallowcopy vs. deepcopy
l=[["ankara","istanbul","samsun"],[6,34,55],100,500,600]#son uc eleman pirimitiv tip
newl=l[:]#shallow

print("ıd l:",id(l))
print("id newl:",id(newl))
# yenı bellek bolgesı acar ve oraya kopyalar.
print("*"*40)
print("ıd l[0]:",id(l[0]))
print("id newl[0]:",id(newl[0]))# referance tiplerin adresini  de kopyalar.
print("*"*80)
newl[0][1]="sinop"
newl[3]=1500#pirimitiv tiplerde ıkısındede kopyalamaz.l de degısmezken newl de degısır

print(" l:",l)
print("newl:",newl)#liste icinde liste olursa adresini de kopyalar.

#deep copy
import copy
newldeep=copy.deepcopy(l)
print("ıd l[0]:",id(l[0]))
print("id newldeep[0]:",id(newldeep[0]))
#deep copy de tum verı tıplerınde adres de degısır
newldeep[0][2]="ordu"
newldeep[2]=5500

print("l:",l)
print("newldeep:",newldeep)

#%%
def double(liste):
    newlist=[]
    for index,value in enumerate(liste):
        newlist.append(value**2)
        
numberlist=[2,4,6,8]
print("fonk cagırmadan once numberlist:",numberlist)
#double(numberlist)
double(numberlist[:])#shallow copy
print("fonk cagırdıktan sonra numberlist:",numberlist)
#herhangi bir referans degerı yoktur.newlıst listeye baglı degıldır.
#%% nested list
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])
print(matrix[2][2])

for row in matrix:
    for value in row:
        print(value,end="\t")
    print()
print("*"*80)
for row in matrix:
    print(row)
#%% liste kavraması
li=[2,4,6,-10,-5,8]
kareli=list(map(lambda x:x**2,li))
print(kareli)

#liste kavraamsı
kareli1=[x**2 for x in li]
print(kareli1)


pozitifkareli=[x**2 for x in li if x>0 ]
print(pozitifkareli)


number= [2,3]
ch=["a","b","c"]
complexlist=[c*n for n in number for c in ch]
print(complexlist)


        

#%%  liste kavraması ornek
name=["ahmet","ayse","ali","mehmet"]
age=[25,5,10,45]
oldlist=[x for i,x in enumerate(name) if age[i]>18]
print(oldlist)






















