import random

#1 - Seleciona valor aleatorio de uma lista

list1 = [7,6,5,4,3,2,1]
print(random.choice(list1))
# 2 - Gera um numero aleatorio em intervalo de valores
r1 = random.randint(1, 60)
print(r1)

#3- seleciona caractere aleatorio de uma string

name = "Curso Python"
r2 = random.choice(name)
print(r2)

# 4- Seleciona mais de um valor aleatorio
#Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(r2, 1))