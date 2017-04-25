def union(A, B):
    return A + setDiff(B, A)

def intersection(A, B):
    return [val for val in A if val in B]

def setDiff(U, A):
    return [val for val in U if val not in A]

def symmDiff(A, B):
    return setDiff(union(A, B), intersection(A, B))#also setDiff(A,B) + setDiff(B,A)

def cartProduct(A, B):
    return [a*b for a in A for b in B] 

#testing
A = [1, 3, 4, 8, 5, 7, 9, 11]
B = [2, 4, 6, 8, 10, 12, 3, 7]
U = range(1,15)
print intersection(A, B)
print setDiff(U, A)
print union(A, B)
print symmDiff(A, B)
print cartProduct(A, B)

