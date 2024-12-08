# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

def find_square(array, k):
    n=len(array)

    for i in range(n):
        for j in range(n):
            for size in range(3,n+1,2):
                half_size=size//2
                if i-half_size>=0 and i+half_size<n and j-half_size>=0 and j+half_size<n:
                    left_upper=array[i-half_size][j-half_size]
                    right_upper=array[i-half_size][j+half_size]
                    left_down=array[i+half_size][j-half_size]
                    right_down=array[i+half_size][j+half_size]
                    if left_upper*right_upper*left_down*right_down==k:
                        return True, (i,j)
    return False, None

T=[[7, 4, 8, 5, 7],
[3, 7 , 8, 5, 4],
[2, 8, 3, 6, 5],
[2, 8, 6, 2, 5],
[5, 6, 1, 1, 3]]
k=30

print(find_square(T,k))