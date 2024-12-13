# Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.

import math
from itertools import combinations

def calculate_distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def calculate_center(points):
    n=len(points)
    sum_x=sum(x for x, y in points)
    sum_y=sum(y for x, y in points)
    return (sum_x/n, sum_y/n)

T=[(3.78, -8.37), (7.06, -4.7), (-9.27, -3.53), (9.85, -2.24), (-6.95, 4.19), (-0.59, -8.15)]


def solve(T):
    centers_of_gravity=[]
    n=len(T)

    for i in range(1,n+1):
        for combination in combinations(T,i):
            center=calculate_center(combination)
            centers_of_gravity.append(center)

    m=len(centers_of_gravity)
    min_distance=float('inf')
    for i in range(m):
        for j in range(i+1, m):
            distance=calculate_distance(centers_of_gravity[i],centers_of_gravity[j])
            min_distance=min(distance,min_distance)

    return min_distance
            
    


    

