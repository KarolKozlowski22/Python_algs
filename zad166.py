from itertools import permutations

def solve(seq1, seq2):
    seq1="".join(seq1)
    for perm in permutations(seq2):
        current_perm="".join(perm)
        if sorted(current_perm)==sorted(seq1):
            return True
    return False

    

    

seq1=["ab","cde","cfed","fab"]
seq2=["abc","abc","def","fed"]
print(solve(seq1,seq2))