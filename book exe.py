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

import math
print(math.sqrt(9))
print(math.pi)

print(math.floor(2.45))










