# Dana jest tablica int t[N][N] wypełniona przypadkowymi wartościami. Proszę napisać
# funkcję, która dla zmiennej typu tablica zwraca numer wiersza w którym występuje najdłuższy spójny
# fragment złożony z liczb o tej samej wartości. W przypadku kilku fragmentów o tej samej długości należy
# zwrócić pozycję pierwszego z nich.

import random

def find(T):
    n=len(T)
    max_length=0
    row_num=-1
    for i in range(n):
        temp=T[i][0]
        temp_length=1
        for j in range(n):
            if T[i][j]==temp:
                temp_length+=1
            else:
                temp=T[i][j]
                temp_length=1
            if temp_length>max_length:
                max_length=temp_length
                row_num=i

    return row_num



if __name__ == "__main__":
    n=8
    T=[[random.randint(0,5) for _ in range(n)] for _ in range(n)]
    print(T)
    print(find(T))