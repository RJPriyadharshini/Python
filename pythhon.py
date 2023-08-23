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





