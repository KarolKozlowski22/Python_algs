# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
# pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była liczbą pierwszą.
# Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na 23 i 47, natomiast divide(2255)=False.
# Przykładowe wywołania funkcji:
# print(divide(273)) # True, podział 2|7|3
# print(divide(22222)) # True, podział 2|2|2|2|2
# print(divide(23672)) # True, po
# podział 23|67|2
# print(divide(2222)) # False
# print(divide(21722)) # False'''

import math

def is_prime(num):
    if num<2:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    
    return True


def solve(num, idx=0, num_of_parts=0):
    if idx==len(num):
        return is_prime(num_of_parts)
    
    for i in range(idx+1, len(num)+1):
        current_num=int(num[idx:i])
        if is_prime(current_num) and solve(num, i, num_of_parts+1):
            return True
    return False

if __name__=="__main__":

    print(solve("273")) # True, podział 2|7|3
    print(solve("22222")) # True, podział 2|2|2|2|2
    print(solve("23672")) # True, po podział 23|67|2
    print(solve("2222")) # False
    print(solve("21722")) # False''