import os
os.system("cls")

def func(n) -> int:
    s = 0
    k = 1
    for i in range(1, n+1):
        s += i
        k *= i
    return s, k
    

def salom_ber(n:int):
    for i in range(n):
        print("Hello world")

a,b = func(5)
print(a,b)