import sys
import math
sys.stdin = open("a_example", 'r')
[M, T2, T3, T4] =  list(map(int, input().split()))
print(M,T2,T3,T4)
pizzas = []
for i in range(M):
    pizzas.append(tuple(input().split()))
two_combi = []
for i in range(len(pizzas)):
    for j in range(i+1, len(pizzas)):
        #if i != j:
            pizza1 = pizzas[i]
            pizza2 = pizzas[j]
            two_combi.append([len(set(pizza1[1:] + pizza2[1:])),(i, j)])
three_combi = []
for i in range(len(pizzas)):
    for j in range(i+1, len(pizzas)):
        for k in range(j+1, len(pizzas)):
            # if i != j and j!= k and i != k:
            pizza1 = pizzas[i]
            pizza2 = pizzas[j]
            pizza3 = pizzas[k]
            three_combi.append([len(set(pizza1[1:] + pizza2[1:] + pizza3[1:])),(i, j, k)])
four_combi = []
for i in range(len(pizzas)):
    for j in range(i+1, len(pizzas)):
        for k in range(j+1, len(pizzas)):
            for x in range(k+1, len(pizzas)):
                pizza1 = pizzas[i]
                pizza2 = pizzas[j]
                pizza3 = pizzas[k]
                pizza4 = pizzas[x]
                four_combi.append([len(set(pizza1[1:] + pizza2[1:] + pizza3[1:] + pizza4[1:])),(i, j, k, x)])
print(pizzas)
print(two_combi)
print()
print()
print(three_combi)
print()
print()
print(four_combi)
print()
print()