
kelime = input("Bir karakter dizisi girin: ")
ters_kelime = ""
uzunluk=len(kelime)

for i in range(uzunluk- 1, -1, -1):
    ters_kelime += kelime[i]

print("Tersten yazılmış hali:", ters_kelime)
