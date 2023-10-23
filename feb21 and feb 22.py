# Standard modules
#  datetime , math , os, sys , copy ,collections
import datetime as dtm
doi=dtm.date(1947,8,15)
dor=dtm.date(1950,1,26)
print(doi,dor)
print(doi.year)
print(dor.month)
print(dor.day)
print(type(doi))
print(doi.isoformat()) #converts the date type to string data type
print(type(doi.isoformat()))
print(type(doi))
print(doi>dor)
print(doi!=dor)

""" DATE FORMAT SPECIFIER
%d - day , %m - month , %y - two digit year , %Y - Four digit year
%a - short week in text , %A - long week in text
%b- short month in text , % B - long month in text """
print("DATE FORMAT SPECIFIER")

print(doi.strftime("%d-%m-%Y"))  #String format time
print(doi.strftime("%dth-%B-%Y"))
dept=dtm.time(10,20)   #hh:mm:ss if seconds not there 0 will assign
print(dept)
log=dtm.datetime(1947,8,15,12,0)
print(log)

print(doi.strftime("%H-%b-%A"))
print(dtm.datetime.now())

#  timestamp: anydate as no.of.seconds , calculated from 1 jan 1970

print(dtm.date.fromtimestamp(19991234567))  # convert timestamp to proper readable date



##### MATH   mathematical fun

import cmath

print(dir(cmath))

print(cmath.pi)
print(cmath.sin(60))
print(cmath.log(1))



### sys

import sys   # manage system related tasks
print(dir(sys))
print(sys.winver)
print(sys.stdin)


#os

import os
print(dir(os))
print(os.listdir())

filenames=os.listdir()
for k in filenames:
    if "Cal" in k:
        print(k)

print(os.getcwd())


## collections

import collections as col
x=(1,2,3)
print(x[0])
marks=col.namedtuple("marks","maths physics biology") # create tuple value with name
shiva=marks(90,60,70)
print(shiva)
print(shiva.maths)


mylist=[1,2,3,4,1,2,5,6,7,8,8,8,8]  # occurence of one number present and their count

print(col.Counter(mylist))

class marks:
    def __init__(self,maths,phy,bio):
        self.maths=maths
        self.phy=phy
        self.bio=bio

obj=marks(80,85,94)
print(obj.maths)


c=[10,2,3,34,45]
print(c.pop())
print(c)

class new(str):
    def show(self):
        for k in self:
            print(k)

x=new("oii")
print(x)
print(x.show())

empjob={"name":"raja","Salary":20000,"desig":"Tester"}
empper={"name":"raja","location":"chennai","contact":93245665587}

emp=col.ChainMap(empjob,empper)
print(emp)     # Chainmap - remove duplicates , only print the 1st occurence of duplicate key

for j,k in emp.items():
    print(j,k)  #  remove duplicates

##lookup

from collections import ChainMap

fruits_price = {"apple":100,"grapes":50,"orange":75} #item:price
veggies_price = {"tomato":15,"brinjal":30,"onion":40}

pricelist = ChainMap(fruits_price , veggies_price)
order = {"apple":4 , "tomato":8,"orange":4} #item:quantity

for item,qty in order.items():
    price=pricelist[item]
    subtotal=qty*price
    print(f'{item:}: Rs.{price:} * {qty} = Rs.{subtotal:}')

pnames=["Pavithra","Arun","Raja","July"]
def names(x):
    for k in x:
        j= pnames[0:4]
        return j  # yield return the value and pass the fun

obj=names(pnames)
print(obj)


num=5
fact=0
if num==5:
    fact=num*(num+1)
    print(fact)

