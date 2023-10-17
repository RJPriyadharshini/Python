#FEB 10

def ids(x):
    for k in range(x):
        print(f'NUM {k}')



# by using YIELD keyword we can pause the function , yield keyword it could store the function in the memory
#whenever we need we can call the fun by using obj or variable
def ids(x):
    for k in range(x):
        yield f'NUM {k}'    #pause the function

obj1=ids(5)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))         #whenever we want at that time , we call
print(next(obj1))



# OOPS (OBJECT ORIENTED PROGRAM)


# Functinal programming
''' 1.writing the program or a fun, which has a small , single objective
2.never use loops or iteration
3.one fun can use another fun to perform complex tasks
4.Non Dependence

python supports functional programmimg '''


x = [10, 20, 30, 40]
def fun(x):
    return x+5

print(fun(7))

#lambda - map take multiple elements,iterable

print(list(map(fun, x)))

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
print(list(map(lambda t:t+5,c)))
x=(list(map(lambda t:t+5,c)))  #single time use lambda(temp fun , not stored in the memory)
print(sum(x))

#lambda - support functional program

s=lambda x,y:x if x>y else y       # used comprehension( we can give only one condition is allowed)
print(s(10,5))




# constructor = specialized function

class datetime:
    def __init__(self, d, m,y):      #constructor , initializer
        self.d = d
        self.m = m
        self.y = y
    def __repr__(self):               #represental
        return f'{self.d}/{self.m}/{self.y}'

obj=datetime(1,3,2000)
print(obj)
# __ __ called dunder methods or magic methods

x=5
y=10
print(dir(x))         # display all the functions
print(x.__add__(y))
print(x.__mul__(y))


class cal():
    def __mul__(self):

