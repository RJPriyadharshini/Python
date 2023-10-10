#1  Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False
def list(values):
    if values.count(19)==2 and values.count(5)>=3:
        print("True")
    else:
        print("False")
list([19,5,5,5,5,19,5,7])


#2  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.

lst=[19, 13, 12, 5, 5, 5, 5, 7]
if len(lst) == 8 and lst[4] == lst[5] == lst[6]:
    print("True")
else:
    print("False")

# 3   Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False
def list(values):
    if all(x in range(0, 991, 10) for x in values):
        return True
    else:
        return False
result=list([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990])
print(result)

#current time
import datetime
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Write a Python program that calculates the area of a circle based on the radius entered by the user.
r=1.1
area=3.14 *r*r
print(round(area,2))

#Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included)
x = []
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        x.append(num)

print(x if x else "None")

#Write a Python program to construct the following pattern, using a nested for loop
#   *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5
for i in range(1, rows + 1):    # 1,2,3,4,5
    print('* ' * i)
for i in range(rows - 1, 0, -1):   # 4,3,2,1
    print('* ' * i)

# Write a Python program that accepts a word from the user and reverses it.
inp=input("enter input: ")
x=inp[::-1]
print(x)





