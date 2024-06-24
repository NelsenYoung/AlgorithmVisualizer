import math

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(array[p + 1 - 1])
    
    for j in range(n2):
        R.append(array[q + j])
    
    L[n1 + 1] = 999999999999999999
    R[n2 + 1] = 999999999999999999

    i = 1
    j = 1

    for k in range(r-p):
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1
    return array

def Merge_Sort(A, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        final = Merge(A, p, q, r)
        return final