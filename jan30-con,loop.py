year = input("Enter year: ")     # DOUBT
leap_year=input(year+" is leap year Y/N: ")
months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")
for month in months:
    if month == "feb" and leap_year in ('y',"Y"):
        date=29
    else:
        date = 28
    if month in ("jan", "mar", "may", "jul", "aug", "oct", "dec"):
        date = 31
    if month in ("apr","jun","sep","nov"):
         date = 30
i = 1
print(month)
monthdate=""
while i <= date:
    monthdate=monthdate+""+str(i)
    i += 1
print(monthdate)




n={10,20,30,40,40,50,10}
print(n)         #set not print or allow duplicate values

m=[1,2,3,4,4,1]
print(list(set(m)))    #change list into set                #sets are unordered     #in sets not define index


a={1,2,3,4,5,6,7,8}
b={3,4,8}
print(b.issubset(a))

# subset means if the subset only contains the value which is present in set
# use remove method  # add elements   # not sliceable

name={"ram","raja","meena","ganesh","ravi"}
bro={"ravi","meenama","zyra","divya","sanju"}
print(name.union(bro))       # remove duplicates unique values
print(name.intersection(bro))   # common values on both
print(name.difference(bro))    # difference only in name
print(name.symmetric_difference(bro)) # differences in both
print(name.update(bro))   # update the list (union)

a={1,2,3,4,5}
b={1,2,3}
diff=a.difference(b)
print(diff)


# multiply two numbers without using *

x=int(input("enter a number1: "))   #10
y=int(input("enter a number2: "))   #15
a=0
b=0
while a<x:    #repeative addition
    z=b+y     # 15  (15+15=30)   (30+15=45)
    b=z       #15    30
    a+=1      # one time
    print(z)  # 15
print(z)

#divide two numbers without using /

x=int(input("enter a number1: "))  # 10
y=int(input("enter a number2: "))  #5
a=1
b=x
while a<x:
    z=b-y       # 10-5=5
    b=z         # 5
    if b<y:
        break
    a+=1
print(f' quotitent of a is {a}')
print(f' quotitent of a is {b}')



