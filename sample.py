string = "Guvi Geeks Network Private Limited"
vowels = ["a", "e", "i", "o", "u"]
z = ""

for i in string:
    if i not in vowels:
        z = z + i
print(z)


# 2 Create a pyramid of numbers from 1 to 20 using for loop

for pyramid in range(1,22):      # 1 2 3 4
    for i in range(1,pyramid):      # 0,1 0,2 0,3
        print(i, end = " ")
    print()

# 3 create a fun that takes a string and returns a new string with all the vowels removed



def fun(string):
    y = ""
    vowels = ["a", "e", "i", "o", "u"]
    for i in string:
        if i not in vowels:
            y=y+i
    print(y)
fun("Priyadharshini")



# 4 create a fun that takes a string and returns a number of unique char in it

def fun(string):      #
    j=""
    for i in string:
        if i not in j:
            j=j+i
    print(j)
fun("Guvi Geeks Network Private Limited")


# 9 write a fun that takes a string and returns number of words in it

def function(*list):
    count = 0  # Initialize a counter for strings
    for i in list:
        if type(i) == str:  # Check if the element is a string
            count += 1  # Increment the counter
    print(count)
function("pavi", "priya", "praveen", "janagi", 1, 2, 3, 4, 5)

#  write a fun that takes a str and returns most frequent char in it

def fun(char):
    z=""
    for i in char:
        if type(i) == str:
            z=z+i
    print(z)

char=("a","e","e","i","i","o","z","i",1,2,3,4,5)





















