A = [1, 3, 4, 5, 7] 
def missing(A): 
    x = [A[i] + 1 for i in range (len(A)-1) if A[i+1] != A[i] + 1]
    return x
print(missing(A))