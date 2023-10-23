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

y="hi buddy its cool"
a=y.split()
print(a)
z=" ".join(a)
print(z)

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

rows = 5
for j in range(1, rows + 1):
    print("* " * j)


a=[2,5,3,4]
a[2:2]=[2]
print(a)

my_dict={"a":1,"b": 2,"c":3}
result=my_dict.values()
print(result)


i=0
while i<3:  #0  1   2
    print(i)    #0  1   2    (0,2,1,3,2,4)
    i=i+1    #1   2   3
    print(i+1)  #2   3   4
