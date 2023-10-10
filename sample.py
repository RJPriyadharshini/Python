# check num odd or even
"""count=0
while count<3:
    number = int(input("enter number: "))
    count = count + 1
    if number%2==0:
        print("Even")
    else:
        print("Odd")"""

#max num

"""num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
if num1>num2:
    print(f'The maximun num is : {num1}')
else:
    print(f'The maximun num is : {num2}')
"""

#prime num check

"""def prime(num):
    if num<1:
        print("Not valid")
    for i in range(2,num):
        if num%i==0:
            return False
    return True
num=int(input("enter num: "))
if prime(num):
    print(f'{num} is prime')
else:
    print(f'{num} is not prime')"""


#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.

"""def find(num):
        for q in num:
            i=[]
            if q%2==0:
                i.append(q)
                print(q)

find(range(1000,3001))    """


#Question:
"""Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3   """

"""def cal(letter,digits):
    print(len(letter.strip(" ")))
    print(len(digits))

cal("hello world","123")
"""


rows = 20

# Create a for loop to iterate over the rows
for i in range(1, rows + 1):
    # Create a nested for loop to iterate over the columns
    for j in range(1, i + 1):
        # Print the current number
        print(j, end=" ")

    # Print a new line at the end of each row
    print()











