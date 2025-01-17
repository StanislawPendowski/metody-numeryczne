def horner(liczba,x):
    w = int(liczba[0])
    for i in range(1,len(liczba)):
        w = x * w + int(liczba[i])
    return w


liczby8 = []
with open('liczby1.txt') as plik:
    for linia in plik:
        liczby8.append(linia.strip())
liczby10 = []
with open('liczby2.txt') as plik:
    for linia in plik:
        liczby10.append(linia)
print(liczby10)

minimum = int(liczby8[0])
maks = int(liczby8[0])

for i in range(1, len(liczby8)):
    if minimum > int(liczby8[i]):
        minimum = int(liczby8[i])
    if maks < int(liczby8[i]):
        maks = int(liczby8[i])
print(minimum, maks)

pierwszy = int(liczby8[0])
pierwszyMaks = pierwszy
ilosc = 1
for i in range(len(liczby8)-1):
    if int(liczby8[i])<=(liczby8[i+1]):
        ilosc += 1
        if ilosc > maksymalnaIlosc:
            maksymalnaIlosc = ilosc
            pierwszyMaks = pierwszy
    else:
        pierwszy = int(liczby8[i])
        ilosc = 1
print(maksymalnaIlosc, pierwszyMaks)

licznik = 0
licznik2 = 0
for i in range(len(liczby8)):
    if horner(liczby8[i],8) == liczby10[i]:
        licznik += 1
    if horner(liczby8[i],8) > liczby10[i]:
        licznik2 += 1
print(licznik, licznik2)