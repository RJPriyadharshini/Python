"""fabonnic
x,y=0,1
while y<50:
    print(y)
    x,y=y,x+y


for i in range(0,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
        continue
    elif i%3==0:
        print("Fizz")
        continue
    elif i%5==0:
        print("Bizz")
        continue
    print(i)

letter="pavithra4567"
count=digit=0
for i in letter:
    if i.isalpha():
        count+=1
    elif i.isdigit():
        digit+=1
print(f'count is {count} and digit is {digit}')

def password(passcode):
    lower = any(char.islower() for char in passcode)
    upper = any(char.isupper() for char in passcode)
    digit = any(char.isdigit() for char in passcode)
    sym = any(char in "!@#$%^&*()_+><?}{|}" for char in passcode)
    return lower and upper and digit and sym and len(passcode) >= 8

obj1 = password("Asx@34455")
obj2 = password("sx@34455")
print(f'{password} {obj1}')
print(obj2)
"""

f = open("bill.txt", 'r')
print(f)
print(f.name)

r=[20,40,60,80]
r[1:4]= []
print(r)