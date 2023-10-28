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
    num = i
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










