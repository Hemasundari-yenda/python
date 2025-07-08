# inheritance
# single level inheritance
class a:
    def sound(self):
        print('this is sound method from class a')
class b(a):
    def smell(self):
        print('this is smell method from class b')
s1=b()
s1.sound()
s1.smell()

#multi level inheritance
class A:
    def f1(self):
        print('the f1 is working')
    def f2(self):
        print('the f2 is working')
class B(A):
    def f3(self):
        print('the f3 is working')
class C(B):
    def f4(self):
        print('the f4 is working')
    def f5(self):
        print('the f5 is working')



a1=A()
a1.f1()
a1.f2()
b1=B()
b1.f2()
b1.f1()
b1.f3()
c1=C()
c1.f1()

#multiple  inheritance
class A:
    def f1(self):
        print('the f1 is working')
    def f2(self):
        print('the f2 is working')
class B:
    def f3(self):
        print('the f3 is working')
class C(A,B):
    def f4(self):
        print('the f4 is working')
    def f5(self):
        print('the f5 is working')
a1=A()
b1=B()
c1=C()
a1.f2()
a1.f1()
b1.f3()
c1.f3()
c1.f1()
c1.f2()
c1.f4()
c1.f5()



