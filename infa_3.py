a = 0
b = 2
E = 1000
całka = 0
szer = (b-a)/E

def f(x):
    return x*x + 1

for i in range(E):
    wys = f(a + i * szer)
    całka += szer * wys

print(całka)
