import sys
import math
sys.stdin = open("a_example", 'r')
[M, T2, T3, T4] =  list(map(int, input().split()))
print(M,T2,T3,T4)
pizzas = []
for i in range(M):
    pizzas.append(tuple(input().split()))


