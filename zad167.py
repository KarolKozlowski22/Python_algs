# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na co najmniej
# dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
# zwraca liczbę sposobów pocięcia słowa na kawałki.

vowels=['a', 'e', 'i', 'o', 'u', 'y']

input="banana"
result=[]
curr_cut=""
for i in range(len(input)):
    if input[i] not in vowels:
        curr_cut+=input[i]
    else:
        curr_cut+=input[i]
        result.append(curr_cut)
        curr_cut=""
print(result)