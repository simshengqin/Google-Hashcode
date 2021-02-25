#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Python code to sort the lists using the second element of sublists 
# Inplace way to sort, use of third variable 
def Sort(sub_li): 
    l = len(sub_li) 
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 

import sys
import math
files = ["a","b","c","d","e","f"]

for fname in files:
    file1 = open("real/" + fname + ".txt", 'r')
    [D,I,S,V,F] =  list(map(int, file1.readline().split()))
    intersections = {}
    cars = []


    for i in range(S):
        [B,E,street_name,L] =  list(file1.readline().split())
        intersections[street_name] = [B,E,L]

    for i in range(V):
        # for each car
        arr =  list(file1.readline().split())
        cars.append(arr)
        time_needed = 0
        for j in range(2, int(arr[0]) + 1):
            # the path of the car
            road = arr[j]
            time_needed += int(intersections[road][2])
        arr.insert(1,time_needed)

    cars = Sort(cars)
    schedule = {} # intersection: [(street,seconds), (street,seconds)]

    for i in range(V):
        # prioritise cars with shortest travel first
        arr = cars[i]
        current_time = 0

        for j in range(2, len(arr)):
            streetname = arr[j]
            intersection = intersections[streetname][1]
            if intersection not in schedule:
                schedule[intersection] = [(streetname, 1)]

    ## print result
    result = []
    result.append(len(schedule))
    for key, value in schedule.items():
        result.append(key)
        result.append(len(value))
        for street, second in value:
            result.append(street + " " + str(second))
    
    f = open("real/" + fname + "1.txt", "w")
    
    for i in result:
        f.write(str(i) + "\n")

    f.close()
    
    print("real/" + fname + "1.txt")


# In[12]:


for i in result:
    print(i)


# In[14]:


f = open("real/b1.txt", "w")

for i in result:
    f.write(str(i))

f.close()


# In[ ]:




