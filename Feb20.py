# EXCEPTIONS
"""try:
 amt=(int(input("enter amount to withdraw: ")))
except:
 print("error, enter numbers only")
else:
 print(f'{amt}')
 print("Withdraw Sucessfully")



amt=input("enter amount to withdraw: ")
if amt.isnumeric():
 amt=int(amt)
 print("withdraw sucessfully")
else:
 print("error")




try:
 amt = (int(input("enter amount: ")))
 f=open("hello.txt",'r')
except FileNotFoundError:
 print("not file found")
except ValueError:
 print("Enter Number only")
else:
 print("None")
finally:
 print("Finally Executed")



num=input("enter num: ")
if type(num)!=int:
    raise Exception("Not allowed")      # raise exception
else:
    print(f'{num}')"""

#exp date
exp=[2021,2022,2023,2024,2025]
for z in exp:
    if z>=2023:
        print(f'Dispatch {z} for place')

#Assert will use - if the condition is true it will execute or it throughs an error
exp=[2031,2032,2033,2034,2035]
for x in exp:
    assert x>2030, 'Alert ****** expired medicine **** ALERT'
    print(f' {x} - market')







