

name="ahmet"
print(name[0])
print(name[2:])
print(name[:2])
print(name[-1])
print(name[:-1])#son karakter dahil degil. 0 dan baslar 
print(name[::-1])#tersini alır
print(name[-4:-2])
print(name[2:len(name)])
#%%
message="merhaba"
for i in range(len(message)):
    print(i,message[i],sep="-")#araya karakter koymak ıstıyorsak sep kullanmalıyız
for i in message:
    print(i,end="  ")
    
for i,ch in enumerate(message):# enumarete indisleme yontemi
    print(i,ch,sep="-")
#%%
prefixes="JKLMNOPQ"
suffix="ack"
for ch in prefixes:
    print(ch,suffix,sep="")
#%%
parola=input("parola girin:")
if(parola.lower()=="abc".lower()):# LOWER buyuk kucuk harf duyarlılıgı saglaar
    print("parola dogru")
else:
    print("parola yanlış")
#%%
message="Nerhaba"
message="m"+message[1:]
print(message)
#%%
def sesli_cikar(str):
    vowels="aeioöuüAEIİUÜÖO"
    newstr=""
    for ch in str:
        if(not ch in vowels):#if(ch not in vowels):
            newstr+=ch
    return newstr
sesli_cikar("merhaba")


#%%
def findindex(str,ch):
    finded=[]
    for index,k in enumerate(str):
        if(k==ch): finded.append(index)
    if(len(finded)>0): return finded
    else: return -1
    
findindex("merhaba","e")
#%%
def count(str,ch):
    number=0
    for k in str:
        if(k==ch):
            number+=1
    return number
print(count("merhaba","a"))
#%%
import string
x=string.ascii_letters
print(type(x),x)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
#%%
import string
while(True):
    name=input("input name:")
    control=True
    for ch in name:
        if(ch not in string.ascii_letters ):
            print("yanlış karakter")
            control=False
            break
    if(control): break
print("name true")
#%%
import string
def islower(ch):
    if(ch in string.ascii_lowercase):
        return True
    else: return False
    
print(islower("c"))
print(islower("A"))
# odev: bu ornek turkce karakterler ıcın de calıssacak
# sonuna turkce karakterler ekleyerek de yapabılıriz
#%%
def count_alphabets(s):
    alphabet =string.ascii_letters 
    alphabet_count = {char: 0 for char in alphabet}   
    for char in s:
        if char in alphabet:
            alphabet_count[char] += 1
    return alphabet_count
result = count_alphabets("Enes")
for char, count in result.items():
    print(f"'{char}': {count} kez geçiyor.")

























    



