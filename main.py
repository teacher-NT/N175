import os
os.system("cls")

class A:
    def func(self):
        print("A")

class B(A):
    def func(self):
        print("B")

class C(B, A):
    pass

class D(C, A):
    pass

class E(D, A):
    pass

e1 =  E()
e1.func()
