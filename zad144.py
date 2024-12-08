# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.

def solve(array, n, target_product):
    length=len(array)
    count=0
    for i in range(length-n+1):
        product=1
        for j in range(i,i+n):
            product*=array[j]
        if product==target_product:
            count+=1
    return count

def solve_reccur(array,i,target_product, n):
    if i>len(array)-n:
        return 0
    product=1
    for j in range(i,i+n):
        product*=array[j]
    current_count=1 if product==target_product else 0
    return current_count+solve_reccur(array,i+1,target_product,n)



array=[1,2,3,4,6,2]
n=2
target_product=12

print(solve(array, n, target_product))
print(solve_reccur(array,0,target_product,n))