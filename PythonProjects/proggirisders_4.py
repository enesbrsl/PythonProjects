def yaz(str):
    ''' bu fonksıyon kendısıne gonderılen parametreyı ekrana 5 defa yazar'''
    #bu alıntı help fonksıyonu ıcın ne anlam ıfade ettıgını acıklar.
    
    print(5*str)
help(yaz)
#burada help dedıgımızde ıcındekı fonksıyonun ıcınde yazan alıntı ekrana yazar
yaz("merhaba")
#%%
def is_divisible_by_2_or_5(n):
    """
    >>> is_divisible_by_2_or_5(8)
    True
    >>> is_divisible_by_2_or_5(7)
    False
    >>> is_divisible_by_2_or_5(5)
    True
    >>> is_divisible_by_2_or_5(9)
    True
    """# burada false vermesı gerekırken bız bılerek true yazdık . o yuzden consolde hata uyarısı cıkacak
    print (n % 2 == 0 or n % 5 == 0)
is_divisible_by_2_or_5(7)

if __name__ == '__main__':
   import doctest
   doctest.testmod()
#%%ödev
def cat_n_times(s, n):
   """
   >>> cat_n_times(’Spam’, 7)
   SpamSpamSpamSpamSpamSpamSpam
   """
   print(s*n)
cat_n_times("Spam",7)
#%%
def is_divisible(x, y):
    #return x % y == 0
    return x % y

print(is_divisible(10, 2))
print(is_divisible(10, 4))

if(not is_divisible(10,2)):#not koyduk nedenı 0 haarıc dıger degerelr true olur bu yuzden bursaı calısmaz.mesele buarada fonk 0 dondurur not da bunu true yapar ve ıfcalısır
    print("bolunebılır")
else: print("bolunemez")
#%%
def print_multiples(n,high):
    i = 1
    while i <= high:
        print (n*i, '\t',end="")
        i += 1
    print()

def print_mult_table(high):
    i = 1
    while i <= high:
        print_multiples(i,high)
        i += 1
# bu fonksıyonlardakı i ler yerel degıskendırler. aynı i degıldır.
print_mult_table(10)
#%%
def fibonacci(kactane):
    i=1
    a, b = 0, 1
    print(a,end=" ")
    while i <kactane:
        print (b, end=" ")
        a, b = b, a+b
        i+=1

fibonacci(5)
#%%
def myabs(x):
    if(x<0):
        return -x
    return x
print(myabs(-5))

def myabs(x):
    if x < 0:
        return -x
    elif x > 0:
        return x

print(myabs(-5))
print(myabs(0))
















































