y = "hi Hello , MAY i Help"
print(y.split(","))
print(y.find("hi", 4))
print(y.replace("hi", "HI"))
print(y.endswith("lp"))

x = " ## How are you %%"
print(x.lstrip("#"))
print(x.rstrip())
print(x.strip("#%"))
print(x.encode())
print(x.partition("H"))

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

rows = 5
for j in range(1, rows + 1):
    print("* " * j)


