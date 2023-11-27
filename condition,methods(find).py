price = 100000
is_good_credit = True
if True:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"down_payment :${down_payment}")

has_high_income = True
has_good_credit = False
if has_good_credit and not has_good_credit:
    print("loan ")
else:
    print("no loan")

temperature = 21
if temperature < 10:
    print("hot day")
elif temperature == 20:
    print("cold day")
else:
    print("none")

name = "Pavithra"
if (len(name)) < 10:
    print("three")
elif (len(name)) > 50:
    print("Fifty")
else:
    print("none")

weight = input("weight:")
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f" you are {converted} kilos")
else:
    converted = weight * 1
    print(f" you are {converted} pounds")


rows = 5
for i in range(rows, 0, -1):         # 5,4,3,2,1
    for j in range(1, i + 1):        # 1,6(5 TIMES) 1,5(4 TIMES)  1,4  1,3  1,2
        print(i, end=" ")
    print()

rows = 5
# reverse loop
for i in range(rows, 0, -1):     # 5,4,3,2,1
    for j in range(0, i):        # 0,5 (5 TIMES)  0,4  0,3  0,2  0,1
        print(j, end=' ')
    print("\r")

age = 18
nationality = "indian"
if age >= 18 and (nationality == "militant" or nationality == "indian"):
    print("true")
else:
    print("false")

x = True
print(type(x))

name = "Pavithra"
p = int(input("enter a physics num: "))
m = int(input("enter a maths num: "))
s = int(input("enter a science num: "))
total = p + m + s
if p>=60 and m>=50 and s>=40:
    print("Greater than marks")
else:
    print("else")
print(f'my name is {name.upper()}')
print(f'Total:{total}')
avg = total / 3
print(f'average marks : {avg/3}')



"""y = "hi Hello , MAY i Help"
print(y.split(","))
print(y.find("hi", 4))
print(y.replace("hi", "HI"))
print(y.endswith("lp"))
print(y.ljust(23,'*'))    # Attach the symbol on that position in right side
print(y.rjust(23,'#'))    # Attach the symbol on that position in lift side
print(y.zfill(22))        # In that position add the 0 value if we didn't specific the value
print(list(enumerate(y)))  # All the values and the position

x = "## How are you %%"
print(x.lstrip("#"))   # remove that value from left side
print(x.rstrip("%"))      # remove that value from right side
print(x.strip("#%"))   # remove from both sides
print(x.encode())
print(x.partition("are"))   # before and after the specific word the partition occur

y="hi buddy its cool"
a=y.split()    # split the value
print(a)
z=" ".join(a)
print(z)

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

rows = 5
for j in range(1, rows + 1):
    print("* " * j)


a=[2,5,3,4]
a[2:2]=[2]
print(a)     # new value addes in center

my_dict={"a":1,"b": 2,"c":3}
result=my_dict.values()
print(result)


i=0
while i<3:  #0  1   2
    print(i)    #0  1   2    (0,2,1,3,2,4)
    i=i+1    #1   2   3
    print(i+1)  #2   3   4
"""

x = 1
r = []

while x == 1:
    user = int(input("Enter a number: "))
    if user != 0:
        r.append(user)
        print(f'sum is {sum(r)}')
        y=sum(r)/len(r)
        print(f'avr is {y}')
    else:
        x = 2

print(r)
print(f'sum is {sum(r)}')
print(f'avr is {y}')

a=[1,2,3,4,5]
print(a[:4].pop())

x = 1
r = 0

while x == 1:
    user = int(input("Enter a number: "))
    if user != 0:
        r=r+user
        print(f'sum is {sum(r)}')
        y=sum(r)/len(r)
        print(f'avr is {y}')
    else:
        x = 2








