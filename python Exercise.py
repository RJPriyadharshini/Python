
"""   1.Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line. """

#   SOLUTION

x = range(2000,3201)
z=[]
for n in x:
  if n%5==0 and n%7!=0:
    z=n
    print(z,end=",")


""" 3 . Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""

#SOLUTION

x = dict()  # Initialize an empty dictionary
for j in range(1, 9):
    z = (j, j*j)
    x[j]= z

print(x)
print(type(x))

"""Question  6:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:"""


def fun(a, b, c, d, e, f, g):
    z = [a, b, c, d, e, f, g]  # Store the arguments in a list
    print(z)

    y = tuple(z)  # Convert the list to a tuple
    print(y)


# Call the function with arguments
fun(11, 12, 13, 14, 14, 16, 17, 18)


"""Question  5:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods."""

# SOLUTION

class myclass:
    def __init__(self, string):
        self.string = string  # Assign the input string to the instance variable
        return string
    def __init__(self,string):
        self.string = string
        print(string.upper())

obj = myclass("donkey")


"""QUESTION 6
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24"""

# SOLUTION
"""C=50
H=30

x=[18,22,24]
for D in x:

Q=[(2 * C * D)/H]
print(Q)"""


#Question 7
#two integer return product if prod less tham 1000 then multiply or sum their

def add(number1,number2):
    x=number1*number2
    if x<=1000:
        print(z)
    else:
        print(number1+number2)
add(20,30)
add(30,40)


#question 8

#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


for i in range(10):          # 0 1  2 3 4 5  6 7  8 9
    if i == 0:
        current_num = 0
        previous_num = 0
    else:
        current_num = i
        previous_num = i - 1
    sum_num = current_num + previous_num

    print(f'Current Number {current_num} Previous Number {previous_num} Sum: {sum_num}')




# question 9
# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
def fun(str):
    if str == "pynative":
        x = str[0::2]   # p n t v
        print("Original String is pynative")
        print("Printing only even index chars")
        for char in x:
            print(char)
    else:
        print("Invalid input")

fun("pynative")

# question 10
"""Write a program to remove characters from a string starting from zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string"""

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))



numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

## question   11
#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

def first_last_same(numberlist):
    num1=numberlist[0]
    num2=numberlist[-1]
    if num1 == num2:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is",first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

@
#question 12ad

#   Iterate the given list of numbers and print only those numbers which are divisible by 5
def list(num):
    l=[]
    for i in num:
        if i%5 == 0:
            print(l.append(i))
            print(f'Given list is {num}')
            print("Divisible by 5")
            for num in l:
                print(l)
        else:
            print("not divisible by 5")

list([10, 20, 33, 46, 55])












