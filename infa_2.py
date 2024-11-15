E = 0.0001
pole = int(input('podaj kwadrat liczby: '))
bok_1 = 1
bok_2 = pole

def wb(x):
    if x < 0:
        return -x
    else:
        return x

while wb(bok_1 - bok_2) > E:
    bok_1 = (bok_1 +bok_2) / 2
    bok_2 = pole/bok_1
    print('bok pierwszy', bok_1)
    print('bok drugi', bok_2)

print('liczba którą podałeś po swierwiastkowaniu wyszłą ', bok_2)

