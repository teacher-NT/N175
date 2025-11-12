import os
os.system("cls")

# sonlar = [12,3,4,15,3,5,44,2,4,8,67]

# def func(n):
#     return n<5

# result = list(filter(func, sonlar))

# print(result)


yoshlar = [12,19,18,20,14]
def func(n):
    return n+1

result = list(map(func, yoshlar))
print(result)