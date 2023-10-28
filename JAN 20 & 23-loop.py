print('1-Account opening')
print('2-Deposit')
print('3-savings')
print('4-Dropped')

choice = int(input("enter a choice: "))
match choice:
    case 1:
        print("Account opening")
    case 2:
        print("Deposit")
    case 3 | 4:
        print("Savings")
    case others:
        print("Invalid one")

"""any thing that should be accessed on element level
indexed,slicing are called iterable object"""

"jan 23 "

x = "hello"
for k in x:
    if k == "o":
        pass
    else:
        print(f'{k} \n')

y = "Done"
for k in y:
    if k != "f":
        print(f'{k},', end=" ")
    else:
        print(y)

a = [1, 2, 3, "Raja", "Rose", 0.4, 5.6]
for c in a:
    if type(c) == str:
        print(c.split(','), "string value")
    elif type(c) == float:
        print(c, "Float ")
    else:
        print()

X = "Hello"
for j in X:
    if j == "l":
        print("j", end="")
    else:
        print(j, end='')

z = "don"
name = "Pavithra"
for n in z:
    print(n)
    print(f'name is:{name}')
    print(f'(Finished) \t')

name = ["Pavi", "Praveen"]
for k in name:
    print(k)
    for j in k:    # inner loop or nested loop
        print(j)
# First k in outer loop execute after that j in k where the j took the each letter in pavi which means four times of
# [p , a, v, i] then the nested loop execute praveen has seven characters so it executes 7 times

list=["@ravi","@raja","@ramu"]
for k in list:
    print(k[1:],end=" ")


