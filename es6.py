from random import randint
listaa = []
Numeri_primi = []
range_lista = []
lista = []
lista.extend(range_lista)
contatore = 0
num_tot = int(input("Da quanti numeri è composta la lista "))
while True:
    if contatore == num_tot:
        break
    else:
        contatore += 1
        n = randint(1, 21)
        listaa.append(n)
print("I", num_tot, "numeri casuali usciti sono i seguenti:")
print(listaa)
for x in listaa:
    print("l'indice di", x, "è", listaa.index(x))
    contatore2 = 0
    while True:
        if contatore2 == len(range(2, x)):
            break
        else:
            for y in range(2, x):
                contatore2 += 1
                if x % y == 0:
                    range_lista.append(x)
    if range_lista == lista:
        print("Il numero", x, "è primo")
        Numeri_primi.append(x)
    else:
        print("Il numero", x, "non è primo")
    range_lista = []
if len(Numeri_primi) >= 1:
    print("I numeri primi,presenti nella lista, sono i seguenti:")
    print(Numeri_primi)
else:
    print("Nella lista non sono presenti numeri primi")