
n=8192
a=n//1000
b=n//100%10
c=n//10%10
d=n%10
print("Numarul este:",n)
print("Ultima cifra a acestui numar:    ", d)
print("Penultima cifra a acestui numar: ", c)
print("Restul impartirii la 9:          ", n%9)
print("Catul impartirii la 9:           ", n/9)
print("Suma cifrelor acestui numar:     ",a+b+c+d)
print("Rasturnatul acestui numar:       ",d*1000+c*100+b*10+a)