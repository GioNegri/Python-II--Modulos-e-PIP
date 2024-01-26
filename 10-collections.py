from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista

fruits = ["Maça","Banana","Uva","Pêra",
          "Uva", "Maça", "Laranja", "Abacaxi",
          "Tangerina",  "Uva" , "Pêra"]

print(fruits)
print(Counter(fruits))

# 2 - utilizando tupla nomeada
game = namedtuple('game',['name','price','note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4", 200, 10.0)
print(g1)
print(g2)

# 3 -Ordenando dicionarios
students = { "Pedro":23, "Ana":22, "Ronaldo":26 }
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

# 4 - Utilizando fila ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)