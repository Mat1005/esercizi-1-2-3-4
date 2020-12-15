lista = []
lista2 = []
n = int(input("Da quanti numeri è composta la lista?"))
for n in range(1,n +1):
    numero =int(input("inserire un numero multiplo di 10"))
    lista.append(numero)
    
    if numero > 30:
        numero2 = numero - numero/2
        lista2.append(numero2)
        
        print("Ecco la lista di numeri,in cui i numeri maggiori di trenta sono stati dimezzati:",lista2)   
      
print("Ecco la lista di numeri:",lista)      


    