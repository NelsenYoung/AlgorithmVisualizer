import math

def Merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []

    i = 0
    j = 0

    for i in range(n1 + 1):
        if i == n1:
            L.append(float('inf'))
        else:
            L.append(array[p + i])
    for j in range(n2 + 1):
        if j == n2:
            R.append(float('inf'))
        else:
            R.append(array[q + j + 1])

    i = 0
    j = 0

    for k in range(r - p + 1):
        if L[i] <= R[j]:
            array[k + p] = L[i]
            i = i + 1
        else:
            array[k + p] = R[j]
            j = j + 1
    return array

def Merge_Sort(A, p, r):
    if p < r:
        q = int(math.floor((p+r)/2))
        Merge_Sort(A, p, q)
        Merge_Sort(A, q+1, r)
        final = Merge(A, p, q, r)
        return final
    
def main():
    print("Input 3 numbers")
    array = []
    number1 = input("Enter number 1: ")
    array.append(int(number1))
    number2 = input("Enter number 2: ")
    array.append(int(number2))
    number3 = input("Enter number 3: ")
    array.append(int(number3))
    
    print(Merge_Sort(array, 1, 3))

if __name__=="__main__": 
    main()