import sys
import math
sys.stdin = open("example.txt", 'r')
[D,I,S,V,F] =  list(map(int, input().split()))
intersections = {}
cars = []
for i in range(S):
    [B,E,street_name,L] =  list(input().split())
    intersections[street_name] = [B,E,L]
for i in range(V):
    arr =  list(input().split())
    cars.append(arr)
print(intersections)
print(cars)