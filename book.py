# 16
"""que1=input("if it is raining ?",  )
if que1=="yes":
    que2=input("if it is windy?", )
    if que2=="yes":
        print("it is too windy for an umbrella")
    else:
        print("take an umbrella")
else:
    print("enjoy your day") """

# 19

"""n=int(input("enter a number: "))
if n<10:
    print("too low")
elif n>=10 and n<=20:
    print("correct")
else:
    print("too high")       """

# strip - remove extra char in the variable
"""text=" #noissues_"
print(text.strip(" # _ "))
print(len(text))  """

# 22
"""first_name=input("enter a first name: ")
sur_nam=input("enter a surname: ")
sur_name=sur_nam.title()
result=first_name + " " + sur_name
print(result)"""

# 25
"""first_name=input("enter a first name: ")
if len(first_name)<5:
    sur_name = input("enter a surname: ")
    result = first_name+sur_name
    print(result.upper())
else:
    print(f'{first_name.lower()}')"""

# 26
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

# 36
""" name = input("enter the name: ")
number=int(input("enter a num: "))
repeated_name = (name + ' ') * number
print(repeated_name, number) """

# 37
""" name = input("enter the name: ")
for i in name:
    print(i)"""

# 40
"""number=int(input("enter a num: "))
if number<50:
    for i in range(50,number,-1):
        print(i)"""

# 42
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

# 44

"""number=int(input("enter a num: "))
if number<=10:
    for i in range(0,number):
        name = input('enter a name: ')
        print(f'{name} has been invited')

else:
    print("More than 10")"""

# 45
"""total=0
while total<=50:
    number = int(input("enter a num: "))
    total = total + number
    print(f'the total is : {total}')"""

# 46


"""i=1
while i<=5:
    number = int(input("enter a num: "))
    i=i+number
    print(number)
    if number > 5:
        print(f'the last number entered was a {number}')"""

# 47
""" num1 = int(input("enter a num: "))
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
    print(s) """

# 48
"""again="y"
count=0
while again=="y":
    name=input("enter name: ")
    
    print(name,"invited")
    count=count+1
    again=input("add another one: ")
print("you have", count,"people coming to party")
"""
# 49
""" import random
num=random.random()
num=num*100
print(num)

num=random.randint(0,8)
print(num)
num=random.randrange(0,100,10)
print(num)

colour=random.choice(["red","blue","green"])
print(colour)

#52
x=random.randint(1,100)
print(x)

#53
fruits=random.choice(["banana","orange","grapes","apple","gauva"])
print(fruits)   """
# 54
"""toss=random.choice(["head","tail"])
user=input("guess value: ")
if toss==user:
    print("you win")
else:
    print("bad luck")
print(toss)"""

# 55

"""num=random.randint(1,6)
user=int(input("pick num: "))
print(num)
if num==user:
    print("well done")
elif user>num:
    print("too high")
    guess=int(input("enter num: "))
    if guess==num:
        print("correct")
    else:
        print("you lose")
elif user<num:
    print("too low")
    guess=int(input("enter guess: "))
    if guess==num:
        print("correct")
    else:
        print("you lose") """

# 56
"""import random
numm=random.randint(1,10)
correct=False
print(numm)
while correct==False:
    guess= int(input("pick num: "))
    if guess==num:
        correct= True"""

"""import turtle
turtle.shape("turtle")
for i in range(0,10):
    turtle.right(36)
    for i in range(0,5):
        turtle.forward(100)
        turtle.right(72)
turtle.exitonclick()     """

# 69


"""country=("India","USA","UK","Europe","China")
print(country)
guess = input("enter country: ")
print(country.index(guess)) """

#70
"""country=("India","USA","UK","Europe","China")
print(country)
guess = input("enter country: ")
print(country.index(guess))
num=int(input("enter 0 to 4: "))
print(country.index(num))  """

# 71

"""list1 = ["ball", "football", "handball", "cricket", "chess", "carrom"]
guess = input("Enter your favorite sport: ")

if guess!=list1:
    list1.append(guess)
    print(sorted(list1))
else:
    print("error")     or """

""" guess = input("Enter your favorite sport: ")
class sports:
    def m1(self,list1):
        if guess != list1:
            list1.append(guess)
            print(sorted(list1))
        else:
            print("error")
obj=sports()
obj.m1(["ball", "football", "handball", "cricket", "chess", "carrom"])  """

#72
"""subject=["eng","tam","mat","sci","soc","his","geo"]
del_sub=input("enter del_sub: ")
new_list = subject.copy()
if del_sub in new_list:
    new_list.remove(del_sub)
    print(new_list)
else:
    print("error") """

# 73




"""class Items:
    def food(self, menu):
        choice = input("Enter food: ")
        removed_item = menu.pop(choice, None)  # Use pop with a default value to avoid KeyError
        if removed_item is not None:
            print(f"You ordered {removed_item}")

        print("Updated Menu:")
        for item, description in menu.items():
            print(f"{item}: {description}")


menu = {"food1": "Chapathi", "food2": "idly", "food3": "dosa"}
obj = Items()
obj.food(menu)  """


#74

""" list=["red","blue","green","yellow","pink","orange","brown","black","white","grey"]
start=int(input("enter start num: "))
end=int(input("enter end num: "))
if list in start.index(list):
    print(i)
elif list not in end.index(list):
    print(j)   """



#75
"""list=[111,222,333,444]
print(list)
num=int(input("enter num: "))
if num in list:
    print(list.index(num))
else:
    print("not in list") """

#76


"""name1=input("enter name: ")
name2=input("enter name: ")
name3=input("enter name: ")
name=[name1,name2,name3]
print(name)
while True:
    user=input("yes or no: ")
    if user=="yes":
        add=input("enter name: ")
        name.append(add)
        print(name)
    else:(
        print("no need")"""

#77

""" name1=input("enter name: ")
name2=input("enter name: ")
name3=input("enter name: ")
name=[name1,name2,name3]
print(name)
user=input("yes or no: ")
if user=="yes":
    add=input("enter name: ")
    name.append(add)
    print(name)
    Index = int(input("enter index: "))
    if 0 <= Index :
        x=name.pop(Index)
        print(x)
        print(name)
    else:
        print("none")
else:
    print("no")  """

#78
""" programms=["chutti","sun","vijay","ktv"]
for i in programms:
    print(i)
show=input("enter show: ")
programms[3] = show  # Replace the third item with the user's input
print(programms) """









