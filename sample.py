string = "Guvi Geeks Network Private Limited"
vowels = ["a", "e", "i", "o", "u"]
z = ""

for i in string:
    if i not in vowels:
        z = z + i
print(z)


# 2 Create a pyramid of numbers from 1 to 20 using for loop

for pyramid in range(1,21):      # 1 2 3 4
    for i in range(1,pyramid-1):     #
        print(i)


