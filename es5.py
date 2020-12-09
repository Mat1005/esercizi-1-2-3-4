Numeri = []
Nndivi3 = []
n = int(input("quanti numeri scriverai?"))
for n in range(1,n +1):
    numero = int(input("scrivi un numero compreso tra 1 e 30 inclusi"))
    Numeri.append(numero)
    divi = numero%3
    if divi > 0 or divi < 0:
        Nndivi3.append(divi)
    else:
        break
print("ecco i numeri che hai scritto",Numeri)
print("ecco i numeri non multipli di tre che hai scritto",Nndivi3)

