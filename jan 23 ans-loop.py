
bill = ["soap,3,13", "brush,15,9", "paste,35,9"]
# billed=["soap,3,13,39","brush,15,9,135","paste,35,9,315"]
i=0
for k in bill:
    y=k.split(",")
    print(y)
    y=int(y[1])*int(y[2])
    k=k+","+str(y)
    bill[i]=k
    i=i+1
print(bill)


address = ['No.3,4th street', '2/19,corner street', '19-16,big street,(via) truck-road']
address1 = []
special = [',', '/', '-', ',', '.']
for i in address:
    for j in special:
        if j in i:
            i = i.replace(str(j), " ")
    address1.append(i)
print(address1)

address = ['No.3,4th street', '2/19,corner street', '19-16,big street,(via) truck-road']
char=[",'/-."]
for k in address:
    for j in k:
        if j in char:
            print("",end="")
        else:
            print(j,end="")
    print("",end="")

# Creating infinite loop not possible in for loop but it possible in while loop
x=0
while x<2:
    m = int(input("enter marks: "))
    if m>50:
        print("greater than 50 and less than 100","mark is " f'{m}')
    elif m<50:
        print("your marks :",m)
    x=x+1





