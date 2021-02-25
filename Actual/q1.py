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
cars_position = []
for i in range(V):
    start_street = cars[i][1]
    cars_position.append([start_street, intersections[start_street][2] + "/" + intersections[start_street][2]])
traffic_lights = []
# 1 is green
for i in range(I):
    traffic_lights.append(1)
for t in range(D):
    
print(cars_position)