import statistics

print(statistics.mean([10, 40, 60]))


def ids(x):
    for k in range(x):
        print(f'NUM {k}')


ids(11)


def id(b):
    for k in range(b):
        yield f'fin{b}'  # DOUBT


a = id(11)
print(a)

# SKIPPED YIELD

# OOPS (OBJECT ORIENTED PROGRAM)

# Functinal programming
''' 1.writing the program or a fun, which has a small , single objective
2.never use loops or iteration
3.one fun can use another fun to perform complex tasks
4.Non Dependence

python supports functional programmimg '''

x = [10, 20, 30, 40]
for k in x:
    print(k)


def fun(c):
    return c + 5


fun(5)
x = [10, 20, 30, 40]
list(map(fun, x))

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


obj = myclass(10, 20) # variable present inside the class which is called as property
obj.add()

# __ __ called dunder methods or magic methods

X=1
y=2

print(dir(X))
print(X.__add__(y))



