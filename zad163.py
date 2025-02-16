# Punkt leżący na płaszczyźnie jest opisywany parą liczb typu float (x,y). Tablica T[N] za
# wiera współrzędne N punktów leżących na płaszczyźnie. Punkty posiadają jednostkową masę. Proszę napisać
#  funkcję, która sprawdza czy istnieje niepusty podzbiór n punktów, gdzie n¡k oraz n jest wielokrotnością liczby
#  3, którego środek ciężkości leży w odległości mniejszej niż r od początku układu współrzędnych. Do funkcji
#  należy przekazać dokładnie 3 parametry: tablicę t, promień r, oraz ogran
# ograniczenie k, funkcja powinna zwrócić
#  wartość typu bool.

from itertools import combinations

def center_of_mass(points):
    n=len(points)
    x_sum=sum(p[0] for p in points)
    y_sum=sum(p[1] for p in points)
    return (x_sum/n, y_sum/n)

def is_in_circle(center, r):
    return (center[0]**2 + center[1]**2)**0.5 < r

def solve(T, r, k):
    N=len(T)

    for n in range(3, N+1, 3):
        if n>k:
            break
        for subset in combinations(T, n):
            center=center_of_mass(subset)
            if is_in_circle(center, r):
                return True
            
    return False


if __name__=="__main__":
    T = [(2, 3), (1, 1), (4, 5), (7, 8), (0, 2), (6, 3), (3, 3)]
    r = 5  # Radius of the circle
    k = 5  # Maximum size of a subset
    print(solve(T, r, k))





