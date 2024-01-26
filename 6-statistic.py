import statistics

# 1 - Aplicar a média

print(statistics.mean([3, 2 , 5 , 8, 9 ]))

# 2 - Aplicar a mediana

print(statistics.median([1 , 3 ,  6 , 8 , 9]))
print(statistics.median([1 , 3 , 5 , 6 , 8 , 9]))

# 3 - Aplicar a moda

print(statistics.mode([1 , 3 , 5 , 6 , 8 , 9, 7,7 , 4 ,6, 5, 6,3]))

# 4 - Desvio padrao
"""
Quanto mais proximo de 0 for o desvio padrao,
significa que os dados do conjunto estao menos dispersos
"""

print(statistics.stdev([1, 1.5 , 2 , 2.5 , 3 , 3.5 , 4 , 4.5]))