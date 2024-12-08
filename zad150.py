# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
# muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
import math

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def solve(num1, num2, i, j, current, primes):
    if i==len(num1) and j==len(num2):
        num=int(current)
        if is_prime(num):
            primes.add(num)
        return 
    if i<len(num1):
        solve(num1,num2,i+1,j,current+num1[i],primes)
    if j<len(num2):
        solve(num1,num2,i,j+1,current+num2[j],primes)

primes=set()
num1=73
num2=75

solve(str(num1), str(num2), 0, 0, "", primes)
print(len(primes))    



