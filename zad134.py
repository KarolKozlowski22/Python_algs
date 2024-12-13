# ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
# naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
# równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

def weight(n):
    if n == 1:
        return 0

    weight = 0
    dividor = 2

    while n > 1:
        if n % dividor == 0:
            weight += 1
            while n % dividor == 0:
                n //= dividor
        dividor += 1
    return weight

def solve(weights, target_sum, subsets, index):
    if index==len(weights):
        return subsets[0]==subsets[1]==subsets[2]==target_sum
    for i in range(3):
        if subsets[i]+weights[index]<=target_sum:
            subsets[i]+=weights[index]
            if solve(weights,target_sum,subsets[i],index+1):
                return True
            subsets[i]-=weights[index]
    return False
    

def make_weights_call_solve(T):
    weights=[weight(el) for el in T]
    weights_sum=sum(weights)
    if weights_sum % 3 !=0:
        return False
    target_sum=weights_sum//3
    return solve(weights,target_sum,[0,0,0],0)

T=[2,4,8]
# T=[2,3,6,30,7]

print(make_weights_call_solve(T))





    
