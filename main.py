def power(A, B):
    if (B == 1):
        return (A)
    if (B != 1):
        return (A * power(A, B - 1))
A = int(input("A: "))
B = int(input("B: "))
print("->", power(A, B))