# single level inheritance
# class A:
#     def m1(self):
#         print('m1 method of class A')
# class B(A):
#     def m2(self):
#         print('m2 mwthod of class B')
# obj1=B()
# obj1.m1()
# obj1.m2()
# multi level inheritace
class A:
    def m1(self):
        print('hi')
class B (A):
    def m2(self):
        print('hello')
class C(B):
    def m3(self):
        print('welcome')
obj1=C()
obj1.m1()
obj1.m2()
obj1.m3()
# multiple inheritance
class A:
    def m1(self):
        print('aman')
class B(A):
    def m2(self):
        print('akshay')
class C(A):
    def m3(self):
        print('shaurya')
