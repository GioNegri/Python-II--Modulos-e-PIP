from random  import randint, random

sorteios = []
contador = 1
while contador <= 50:
    numero = randint(1,100)
    if not numero in sorteios:
        sorteios.append(numero)
        contador = contador + 1
        
sorted_numbers = sorted(sorteios)


print(sorted_numbers)

#print(sorteios)