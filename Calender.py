calender = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

month = input("Enter month: ")

if month in ["jan", "mar", "may", "jul", "aug", "oct", "dec"]:
    days = 31
elif month == "feb":
    year = input("Enter year: ")
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days = 29
    else:
        days = 28
else:
    days = 30

i = 1
while i <= days:
    print(i)
    i += 1

numm = int(input("enter 1st num: "))  # 5*2=10
num = int(input("enter 2nd number: "))
if numm!=988:
    z = (numm + numm)
    print("Your answer is: " f'{z}')
else:
    print("Error")


n={10,20,30,40,40,50,10}
print(n)         #set not print or allow duplicate values
m=[1,2,3,4,4,1]
print(list(set(m)))    #change list into set                #sets are unordered     #in sets not define index


a={1,2,3,4,5,6,7,8}
b={3,4,5}
print(b.issubset(a))

# subset means if the subset only contains the value which is present in set
# use remove method  # add elements   # not sliceable

name={"ram","raja","meena","ganesh","ravi"}
bro={"ravi","meenama","zyra","divya","sanju"}
print(name.union(bro))       # remove duplicates unique values
print(name.intersection(bro))   # common values on both
print(name.difference(bro))    # difference only in name
print(name.symmetric_difference(bro)) # differences in both





