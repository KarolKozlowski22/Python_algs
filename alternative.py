# Aby otrzymać nagrodę trzeba przejść kolejno przez N komnat. W każdej komnacie znajduje się skrzynia (mogąca pomieścić maksymalnie 100 sztabek), w której umieszczono pewną liczbę sztabek złota. 
# Będąc w danej komnacie możemy zabrać ze skrzyni pewną liczbę sztabek albo dołożyć do skrzyni wcześniej zebrane sztabki. Liczba sztabek przenoszona do następnej komnaty nie może przekraczać 6. 
# Drzwi do kolejnej komnaty otwierają się wtedy, gdy liczba sztabek pozostawiona w skrzyni będzie liczbą pierwszą. Z ostatniej komnaty nie wolno wynieść żadnej sztabki. Proszę napisać funkcję, która zwraca informację, 
# czy jest możliwe przejście przez komanty. Do funkcji należy przekazać tablicę zawierającą liczby sztabek w kolejnych komnatach. 
# Na przykład: T = [10, 20, 30] −→ funkcja powinna zwrócić False T = [10, 20, 35] −→ funkcja powinna zwrócić True, w komnatach pozostanie [5, 23, 37]

import math


def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True

def solve(T, idx, gold_in_hand):
    if idx==len(T):
        return gold_in_hand==0
    
    for val in range(0, min(6, T[idx])+1):
        new_gold_in_hand_1=gold_in_hand-val

        if is_prime(T[idx]+val) and new_gold_in_hand_1>=0 and solve(T, idx+1, new_gold_in_hand_1):
            return True
    
        new_gold_in_hand_2=gold_in_hand+val

        if is_prime(T[idx]-val) and new_gold_in_hand_2 <=6 and solve(T, idx+1, new_gold_in_hand_2):
            return True


    return False
    



if __name__=="__main__":
    T_1 = [10, 20, 30]  #False
    T_2 = [10, 20, 35]  #True

    print(solve(T_1, 0, 0))
    print(solve(T_2, 0, 0))

    
    
    

