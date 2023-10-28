"""
x = [1, 2, 2, 3, 4]
y = [i for i in x if i != 2]

print(y)

x = [1, 2, 2, 3, 4]
v = []

for i in x:
    if i != 2:
        v.append(i)
print(v)



x={1,2,3,"gghhh"}
print(x)
x=(1,2,"jyfk")
print(x)



from functools import reduce
k=[1,2,3,4]
y=reduce(lambda a,b:a+a,k)
print(y)"""

#lambda - map take multiple elements,iterable

"""print(list(map(fun, x)))

x=["Dr.Aravind","Raja","Ramu","Dr.Pavi"]
def fun(x):
    if "Dr" in x:
        return True
    else:
        return False

print(list(map(fun,x)))

#filter - filter the value based on condition

print(list(filter(fun,x)))   # True - it add element to the list  or not written

def big(x,y):
    if x>y:
        return x
    else:
        return y

print(big(50,big(20,big(30,40))))    #recursion

c=[10,30,40,100,56]
print(sum(c))
print(list(map(lambda t:t+2,c)))
x=(list(map(lambda t:t+2,c)))  #single time use lambda(temp fun , not stored in the memory)
print(sum(x))

#lambda - support functional program

s=lambda x,y:x if x>y else y       # used comprehension( we can give only one condition is allowed)
print(s(10,5))  """

#GUVI CLASS - DAY 4 PYTHON
def fun():
    return lambda a,b:a+b
g=fun()
print(g(1,5))

x=[1,2,3,4,5]
y=list(map(lambda a:a*2,x))
print(y)

g=[1,2,3,4,5,6]
h=list(filter(lambda a:a>2,g))
print(h)

from functools import reduce
x=[10,20,30,40,50]       # 10+20=30   30+30=60  60+40=100  100+50=150
z=reduce((lambda a,b:a+b),x)
print(z)

# FILE HANDLING
# r -read txt file
# w - write the data into txt file
# a - append - add extra line into the file
# x - create the txt file"""

f=open("guvi.txt","w")
f.write("first line")
f.close()

"""import os
os.remove("text.txt")  """  #remove the text file from os

#list comprehension

a=["apple","banana","orange","grapes"]
z=[i for i in a]
print(z)
x=[i for i in a if i=="banana"]   # based on if condition
print(x)

b=[["mysore","bangalore"],["chennai","salem"]]
z=[i for sublist in b for i in sublist if len(i)>5]
print(z)

#OR
for sublist in b:
    for i in sublist:
        print(i)

#OOPS
#__init__ operator (constructr operator ) whenever we call the call that init operator calls automatically

class parent:
    def __init__(self,a):
        self.a=a
    def f2(self):
        print(self.a)
obj=parent("python")   # passing arguments in 1st fun
obj.f2()   # by calling 2nd fun , 1st fun value prints

#Inheritance - Inherits all the methods and properties from parent to child class
#parent class - independent
#super keyword - used to Inherits all the methods and properties from parent to child class

class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class child(parent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
obj=child(a="python",b="selenium",c="32")
print(obj.a,obj.c)

#POLYMORPHISM - Creating more than one class but same method

class A:
    def f1(self):
        print("A")
class B:
    def f1(self):
        print("B")
class C:
    def f1(self):
        print("C")

x1=A()
x1.f1()
x2=B()
x2.f1()
x3=C()
x3.f1()

#METHOD OVER RIDING

class parent:
    def m(self):
        print("Parent")
class child(parent):
    def m1(self):
        print("child")
obj1=parent()
obj2=child()
obj1.m()
#obj1.m1()
obj2.m1()
obj2.m()


#METHOD OVERLOAD

class myclass:
    def m1(self,a,b=None):
        if b is None:
            return a
        else:
            return a+b
obj=myclass()
print(obj.m1(5))
print(obj.m1(5,10))

# ARRAY RECURSIVE
#array - store multiple values in single variable
#Indexable

array=["car","bike","mouse","Tv"]
print(array[0])
array[2]="phone"
print(array[2])




