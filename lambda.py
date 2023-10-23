


x = [1, 2, 2, 3, 4]
y = [i for i in x if i != 2]

print(y)

x = [1, 2, 2, 3, 4]
v = []

for i in x:
    if i != 2:
        v.append(i)
print(v)






x={1,2,3,"gghhh"}
print(x)
x=(1,2,"jyfk")
print(x)



from functools import reduce
k=[1,2,3,4]
y=reduce(lambda a,b:a+a,k)
print(y)


