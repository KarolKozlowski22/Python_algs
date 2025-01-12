# Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnym ¿1 odbywają się wyścigi wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
# Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wie¿a startuje z prawego
# górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
# lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
# wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
# napisać funkcjˆe, która dla danej tablicy zwraca numer wie¿y, która wygra wyścig lub zero jeżeli wyścig będzie
# nierozstrzygnięty. Można założyć, ¿e podczas wyścigu wieże nie spotkają się na jednym polu

def gcd(a, b):
    if (a == 0):
        return b
    if (b == 0):
        return a
    if (a == b):
        return a
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

def are_coprime(a,b):
    return gcd(a,b)==1

def solve_tower1(T, i, j, n):
    if i==n-1 and j==n-1:
        return 0
    min_moves=float('inf')
    if i+1<n and are_coprime(T[i][j], T[i+1][j]):
        min_moves=min(min_moves, 1+solve_tower1(T,i+1,j,n))
    if j+1<n and are_coprime(T[i][j], T[i][j+1]):
        min_moves=min(min_moves, 1+solve_tower1(T,i,j+1,n))
    return min_moves

def solve_tower2(T, i, j, n):
    if i==n-1 and j==0:
        return 0
    min_moves=float('inf')
    if i+1<n and are_coprime(T[i][j], T[i+1][j]):
        min_moves=min(min_moves, 1+solve_tower2(T,i+1,j,n))
    if j-1>-1 and are_coprime(T[i][j], T[i][j-1]):
        min_moves=min(min_moves, 1+solve_tower2(T,i,j-1,n))
    return min_moves

def win_or_draw(T):
    n=len(T)
    moves1=solve_tower1(T, 0, 0, n)
    moves2=solve_tower2(T, 0, n-1, n)
    print(moves1, moves2)

    if moves1 < moves2:
        return "Wygrywa pierwsza wieża"
    elif moves2 < moves1:
        return "Wygrywa druga wieża"
    else:
        return "Remis"



if __name__ == "__main__":
    T = [
        [3, 7, 5],
        [2, 6, 4],
        [8, 9, 1]
    ]
    print(win_or_draw(T))


