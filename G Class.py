"""
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
print(y)"""

#lambda - map take multiple elements,iterable

"""print(list(map(fun, x)))

x=["Dr.Aravind","Raja","Ramu","Dr.Pavi"]
def fun(x):
    if "Dr" in x:
        return True
    else:
        return False

print(list(map(fun,x)))

#filter - filter the value based on condition

print(list(filter(fun,x)))   # True - it add element to the list  or not written

def big(x,y):
    if x>y:
        return x
    else:
        return y

print(big(50,big(20,big(30,40))))    #recursion

c=[10,30,40,100,56]
print(sum(c))
print(list(map(lambda t:t+2,c)))
x=(list(map(lambda t:t+2,c)))  #single time use lambda(temp fun , not stored in the memory)
print(sum(x))

#lambda - support functional program

s=lambda x,y:x if x>y else y       # used comprehension( we can give only one condition is allowed)
print(s(10,5))  """

#GUVI CLASS - DAY 4 PYTHON
def fun():
    return lambda a,b:a+b
g=fun()
print(g(1,5))

x=[1,2,3,4,5]
y=list(map(lambda a:a*2,x))
print(y)

g=[1,2,3,4,5,6]
h=list(filter(lambda a:a>2,g))
print(h)

from functools import reduce
x=[10,20,30,40,50]       # 10+20=30   30+30=60  60+40=100  100+50=150
z=reduce((lambda a,b:a+b),x)
print(z)

# FILE HANDLING
# r -read txt file
# w - write the data into txt file
# a - append - add extra line into the file
# x - create the txt file"""

f=open("guvi.txt","w")
f.write("first line")
f.close()

"""import os
os.remove("text.txt")  """  #remove the text file from os

#list comprehension

a=["apple","banana","orange","grapes"]
z=[i for i in a]
print(z)
x=[i for i in a if i=="banana"]   # based on if condition
print(x)

b=[["mysore","bangalore"],["chennai","salem"]]
z=[i for sublist in b for i in sublist if len(i)>5]
print(z)

#OR
for sublist in b:
    for i in sublist:
        print(i)

#OOPS
#__init__ operator (constructr operator ) whenever we call the call that init operator calls automatically

class parent:
    def __init__(self,a):
        self.a=a
    def f2(self):
        print(self.a)
obj=parent("python")   # passing arguments in 1st fun
obj.f2()   # by calling 2nd fun , 1st fun value prints

#Inheritance - Inherits all the methods and properties from parent to child class
#parent class - independent
#super keyword - used to Inherits all the methods and properties from parent to child class

class parent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class child(parent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
obj=child(a="python",b="selenium",c="32")
print(obj.a,obj.c)

#POLYMORPHISM - Creating more than one class but same method

class A:
    def f1(self):
        print("A")
class B:
    def f1(self):
        print("B")
class C:
    def f1(self):
        print("C")

x1=A()
x1.f1()
x2=B()
x2.f1()
x3=C()
x3.f1()

#METHOD OVER RIDING

class parent:
    def m(self):
        print("Parent")
class child(parent):
    def m1(self):
        print("child")
obj1=parent()
obj2=child()
obj1.m()
#obj1.m1()
obj2.m1()
obj2.m()


#METHOD OVERLOAD

class myclass:
    def m1(self,a,b=None):
        if b is None:
            return a
        else:
            return a+b
obj=myclass()
print(obj.m1(5))
print(obj.m1(5,10))

# ARRAY RECURSIVE
#array - store multiple values in single variable
#Indexable

array=["car","bike","mouse","Tv"]
print(array[0])
array[2]="phone"
print(array[2])

#iterators  - in form of tuples

# two methods - iter() and  next()

a=(1,2,3,4)
myiter=iter(a)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
a=(1,2,3,4)
class number():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=5:
            x=self.a
            self.a+=1
            return a
        else:
            raise StopIteration
obj=number()
myiter=iter(obj)
for x in myiter:
    print(x)

# Generators - Sequence of results
# with single exp we can make sequence
# syntax - yield[expression list]

def cubes(n):
    result=[]
    for i in range(n):
        g=i**3
        result.append(g)
    return result
print(cubes(10))

# BY USING GENERATORS
def cubes(n):
    for i in range(n):
        yield i**3
print(list(cubes(10)))

# REGULAR EXPRESSIONS
""" ^ - starts with
$ - ends with
* - one or more occurence"""

import re
text="regular expression is of the module in the python"
x=re.search("^regular.*python$",text)
print(x)

x=re.findall("the",text)
print(x)
print(re.search("python",text))

def pallindrome(s):
    s=s.replace(" ","").lower()
    return s ==s[::-1]
if __name__=="__main__":
    input_str=input()
    result=pallindrome(input_str)
    if result:
        print(pallindrome)
    else:
        print("not")

x=(64,65,"A")
Z=max(x)
print(Z)



#HTTP - Hypertext markup language

"""It is not case sensitive
it support all  browsers

HTML ELEMENT    -     start tag and end tag
html element are head , html,h1,p-paragraph

<!DOCTYPE html>  -   declaration defines that this document is an HTML5 document
<tagname>            start and </tagname> ends
example
<h1>                 My first heading</h1>  -font size  bigger
<h6> -               font size smaller
<a                   href="www.google.com" </a>          --- hyperlink
<img> -              image
<scr> -              source
<alt> --            alternative text  , height and weight are provided as attributes

Absolute URL - External image on other website if has copyright we cannot able to download
Relative URL - hosted in website , url does not include domain name

<b> body</b>

<hr>     - horizontal rule , 	Defines a thematic change in the content
<br>       in new line  , empty elements - it doesnt have a end tag(like <br>)
<pre>    - Write inside the paragragh 
style="text-align:center;"          - center alignment 
style="background-color:yellow;"    - set bg color


HTML Formatting Elements

Formatting elements were designed to display special types of text:

<b>           - Bold text
<strong>      - Important text
<i>           - Italic text
<em>          - Emphasized text
<mark>        - Marked text
<small>       - Smaller text
<del>        - Deleted text
<ins>        - Inserted text
<sub>        - Subscript text
<sup>        - Superscript text


HTML Quotation and Citation Elements

<abbr>	        -   abbreviation or acronym
<address>	     -  information for the author/owner of a document
<bdo>	         -  text direction
<blockquote>   -   quoted from another source
<cite>	      -    title of a work
<q>	          -   short inline quotation

<!-- This is a comment -->   for comment 
style="border:2px solid Tomato;"   - borders 

<span>      - give more importance 
Classes    -   used by CSS and JavaScript to access specific elements , case sensitive 
getElementsByClassName() method   - JavaScript can access elements with a specific class name

** DIFF B/W CLASS AND ID

class -  name can be used by multiple HTML elements
id   -  name must only be used by one HTML element within the page:

** iframe **

<iframe>	Defines an inline frame
An HTML iframe is used to display a web page within a web page.

***  HTML head Elements ***

<head>	   -  Defines information about the document
<title>     - Defines the title of a document
<base>	-     Defines a default address or a default target for all links on a page,must have either an href or a target attribute present, or both
<link>	-     Defines the relationship between a document and an external resource
<meta>	-     metadata about an HTML document,The metadata will not be displayed on the page, but is used by browsers 
<script>   -  client-side java script
<style>    - style information for a document  

*** HTML Computer Code Elements ***

<code>	Defines programming code
<kbd>	Defines keyboard input 

***FORM***

Action attribute   -   action to be performed when the form is submitted.
Action attribute is omitted, the action is set to the current page.

Target attribute     -    specifies where to display the response that is received after submitting the form

_blank	             -   The response is displayed in a new window or tab
_self	            -    displayed in the current window
_parent	            -    displayed in the parent frame
_top	            -    displayed in the full body of the window
framename	         -   displayed in a named iframe

EG:

<form action="/action_page.php" target="_blank">


Method attributes -
----used when submitting the form data.
----The form-data can be sent as URL variables (with method="get") or as HTTP post transaction (with method="post").

GET:

----Appends the form data to the URL, in name/value pairs
----Never use GET to send sensitive data! (the submitted form data is visible in the URL!)
----The length of a URL is limited (2048 characters)
----Useful for form submissions 
----non-secure data, like query strings in Google



POST:

----Appends the form data inside the body of the HTTP request (the submitted form data is not shown in the URL)
----POST has no size limitations, and can be used to send large amounts of data.
----Form submissions with POST cannot be bookmarked


Autocomplete Attribute

----form should have autocomplete on or off.
EG:

<form action="/action_page.php" autocomplete="on">

Novalidate Attribute

----boolean attribute.
----form-data (input) should not be validated when submitted.


STYLE ATTRIBUTES


Form elements - diff type of input elements 


<form>	Defines an HTML form for user input
<input>	Defines an input control
<textarea>	Defines a multiline input control (text area)
<label>	Defines a label for an <input> element
<fieldset>	Groups related elements in a form
<legend>	Defines a caption for a <fieldset> element
<select>	Defines a drop-down list
<optgroup>	Defines a group of related options in a drop-down list


<option>	Defines an option in a drop-down list,
default, the first item in the drop-down list is selected.


<button>	Defines a clickable button
<datalist>	Specifies a list of pre-defined options for input controls
<output>	Defines the result of a calculation

Use the size attribute to specify the number of visible values
Use the multiple attribute to allow the user to select more than one value:

<fieldset> -  element is used to group related data in a form.

<legend>   -  element defines a caption for the <fieldset> element.
<datalist>   -  element specifies a list of pre-defined options for an <input> element.
input elements displayed in many ways , depending on the type attribute

<input type="text">     - displays a single line text input
<input type="radio">   - select one of many choices
<input type="checkbox">   - select zero or more of many choices
<input type="submit">     - submit the form
<input type="button">    - clickable button




***TEXT***

<form>
    <label form="fname">First name:</label><br>
    <input form="text" id="fname" name="fname"><br>
    <label form="lname">Last name:</label><br>
    <input form="text" id="lname" name="lname"><br>
    </form>
          
          
*** RADIO***

<input type="radio" id="html" name="fav_language" value="HTML">
<label for="html">HTML</label><br>
<input type="radio" id="css" name="fav_language" value="CSS">
<label for="css">CSS</label><br>
<input type="radio" id="javascript" name="fav_language" value="JavaScript">
<label for="javascript">JavaScript</label><br>

<input type="radio" id="python" name="fav_language" value="python">
<label for="python">python</label>


*** CHECKLIST ***

<input type="checkbox" id="vehicle1" name="vehicle1" value="Bike">
<label for="vehicle1"> I have a bike</label><br>
<input type="checkbox" id="vehicle2" name="vehicle2" value="Car">
<label for="vehicle2"> I have a car</label><br>
<input type="checkbox" id="vehicle3" name="vehicle3" value="Boat">
<label for="vehicle3"> I have a boat</label><br><br>

*** SUBMIT ***
<input type="submit" value="Submit"> 


radio - round   - Choose only one
checklist - square - choose all the options
<form action="/action_page.php" id="form1">  Withput using that form , not perform any action




"""





