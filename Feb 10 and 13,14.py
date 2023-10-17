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

#lambda - map take multiple elements

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


z = [1, 2, 3, 4]
v = []
for v in z:
    v = v + 5
    print(v)

x = [10, 20, 30, 40]
print(list(map(lambda z: z + 5, x)))



gst = lambda price: price * 18 / 100
print(gst(170))


# constructor = specialized function

class myclass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self): #represental
        return (self.x + self.y)



# __ __ called dunder methods or magic methods



