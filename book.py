#16
"""que1=input("if it is raining ?",  )
if que1=="yes":
    que2=input("if it is windy?", )
    if que2=="yes":
        print("it is too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("enjoy your day") """

#19

"""n=int(input("enter a number: "))
if n<10:
    print("too low")
elif n>=10 and n<=20:
    print("correct")
else:
    print("too high")       """

#strip - remove extra char in the variable
"""text=" #noissues_"
print(text.strip(" # _ "))
print(len(text))  """

#22
"""first_name=input("enter a first name: ")
sur_nam=input("enter a surname: ")
sur_name=sur_nam.title()
result=first_name + " " + sur_name
print(result)"""

#25
"""first_name=input("enter a first name: ")
if len(first_name)<5:
    sur_name = input("enter a surname: ")
    result = first_name+sur_name
    print(result.upper())
else:
    print(f'{first_name.lower()}')"""

#26
"""word = input("Enter a word: ")
first= word[0]
length=len(word)
rest = word[1:length]
if first != "a" and first !="e" and first !="i" and first !="o" and first !="u":
    newword=rest + first +"ay"
else:
    newword= word + "way"
print(newword.lower()) """

"""import math
print(math.sqrt(9))
print(math.pi)"""

#36
""" name = input("enter the name: ")
number=int(input("enter a num: "))
repeated_name = (name + ' ') * number
print(repeated_name, number) """

#37
""" name = input("enter the name: ")
for i in name:
    print(i)"""

#40
"""number=int(input("enter a num: "))
if number<50:
    for i in range(50,number,-1):
        print(i)"""

#42
"""total=0
if total<=5:
    num=int(input("enter a num: "))
    total=total+1
print("done")


x = input("Enter 'up': ")
number = int(input("Enter a number: "))

if x == "up":
    if number >= 1:
        i = 1wa
        while i <= number:
            print(i)
            i += 1
    else:
        print("Error: 'number' should be a positive integer.")
else:
    print("None") """

#44

"""number=int(input("enter a num: "))
if number<=10:
    for i in range(0,number):
        name = input('enter a name: ')
        print(f'{name} has been invited')

else:
    print("More than 10")"""


#45
"""total=0
while total<=50:
    number = int(input("enter a num: "))
    total = total + number
    print(f'the total is : {total}')"""

#46


"""i=1
while i<=5:
    number = int(input("enter a num: "))
    i=i+number
    print(number)
    if number > 5:
        print(f'the last number entered was a {number}')"""


#47
num1 = int(input("enter a num: "))
num2 = int(input("enter a num: "))
s=num1+num2
if type(s)==int:
    while type(s)==int:
        user = input("enter another number (y/n): ")
        if user=="n":
            print(s)
            break
        else:
            num = int(input("enter a num: "))
            s=s + num
            print(s)
else:
    print(s)

#48
























