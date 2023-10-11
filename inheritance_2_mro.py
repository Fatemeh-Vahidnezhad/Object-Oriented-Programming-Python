class A:
    pass

class B(A):
    pass


class C(A):
    def func(self):
        print("b")


class D(B,C):
    pass


a = D()
a.func()
print(help(D)) #it shows the order of inheritance
