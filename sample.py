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






