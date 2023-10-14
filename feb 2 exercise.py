# look up   interview questions             DOUBT
fruitprice = {"apple": 40, "potato": 90, "grapes": 50}
vegprice = {"carrot": 60, "potato": 40, "tomato": 80}

cart = {"apple": 4, "potato": 3, "grapes": 3}

print({key:values*fruitprice[key] for key,values in cart.items()})





contacts = {}
for i in range(1, 2):
    phone = input("Enter number: ")
    name = input("Enter name: ")

    # Add the contact to the dictionary
    contacts[name] = phone

print("Contacts:")
for name, phone in contacts.items():
    print(f"{name}: {phone}")

COL=["name","age","salary"]
f=dict.fromkeys(COL,"index")
print(f)

v=[11,22,33,44,55]
for k in v:
    print(k+4)  #another method

print([k+4 for k in v])
#comprehension in python.. multiple statements in single line

print({k+4 for k in v} )
#set comprehension
for k in v:
    if k>22:
        print(k+5)


print([k+5 for k in v if k>22])

X=["dr.ashok","dr.raja","ravi",10,20,40]
print([k for k in X if type(k)==str and "dr" in k])

x=20
y=30
print("equal" if x==y else x if x<y  else y)

name=["sanjay","miru","murali",16,45]
print ([ k for k in name if type(k)==int])

c=["hi","hello","how"]
print([k.upper() for k in c if "o" in k]) # filtered comprehensions

g=[10,60,"none",47,"none"]

print([k+4 if type(k)==int else "NA" for k in g])

dollar={"mouse":10,"keyboard":40}
print ({k:v*82  for k,v in dollar.items()})

x=["name","age","salary"]
y=["pavi",23,20000]
z=dict((zip(x,y)))   # zip combine the data using the index
print(z)






