"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.implicitly_wait(10)
# Amount of time driver should wait to find the element(if you call next condition it perform
# implicitly_wait - it is applicable to all the below statements


driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#XPATH SYNTAX -     //tagname[@Attribute='Value']

actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")


time.sleep(5)

# performance of the script is very poor
# if the element is not available within the time mentioned


driver.close()  """

"""DAY -2
LOCATORS 

Identify elements in the webpage we use locators 

Lacators - id , Name , Linktext, PartialLinktext , ClassName , TagName
Customized Locators - CSS SELECTOR AND  XPATH
CSS SELECTOR - Tag and ID , Tag and class , Tag and attribute , Tag, class and attribute
XPATH - Absolute XPath(Full) , Relative XPath(Partial)

close()  - close only one browser at a time
quit() - close all browsers

HTML STRUCTURE

<input name = "txtUsername" id="txtUsername" type="text"(input is element , name is attribute , txtusername is value
 """
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(20)
driver.maximize_window()
driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()   [both are same we can use link or partial link]
#driver.find_element(By.XPATH,"//a[@lehref='/novo-thinkpad-x1-carbon-laptop']").click()
time.sleep(50)
driver.close()"""

#find elements - find all the elements with same tag  - multiple web elements

"""sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(slider))   -> print the total len of the slider 

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))   total num of links present """

#CSS SELECTORS (tag is optional)

"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.facebook.com/")
driver.implicitly_wait(20)

#TAG AND ID - CSS  [tagname#valueofId]

#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("aba")
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("tag and id")

#TAG AND CLASS  [tagname.valueofclass]

#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Tag and class")
#(actual class value is "inputtext _55r1 _6luy" sometimes we have to remove the text after the space)

#Tag and attribute [tagname[attribute=value]    ]

#driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("tag attributes")

#Tag class and attribute  [ tagname.valueofclass[attribute=value]   ]

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass").send_keys("pass")
#(we have both same tagname and class in that time we have to identify diff attributed for that two selection)

time.sleep(100)
driver.close()   """

#  DAY -3

"""    XPATH (works based on DOM)
-> Finding an element in webpage
-> finding element using HTML DOM Structure
-> navigate through elements and attributes
-> address of the element

DOM-Document object model
->API interface it represents the structure of  HTML and XML Documents as tree structure
->used to locate the web elemets,and creats a DOM of the page


Absolute path (copy full xpath)  - 
->  use only tags / nodes
-> Start from root node

/html/body/nav/div/div[2]/div[2]/ul/li[2]/a/button

Relative path  -
->directly to the element
-> use attributes

//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a/button

Write XPATH Manually:

Absolute xpath
/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a

relative
 //tagname[@Attribute='Value']
 
selectors hub - extension used in chrome,browser (to identify tags)

interview question - Most of the time we use relative XPath because  
- If developer introduced the new element then absolute xpath will be broken
-- if developer changed the location then absolute xpath will be broken
absolute xpath is unstable

XPATH OPTIONS

and 
or
contains
starts-with
text

if the button is "START/STOP" how to identify at that time we use contains or startswith
//*[contains(@id,st)] or //*[starts-with(@id,'st')]   or //*[@id='start' or id='stop'] - in this if you call it start and stop both will execute



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://www.orangehrm.com/")
#relative xpath
driver.find_element(By.XPATH, "//button[@class='btn btn-ohrm btn-free-demo']").click()

driver.quit()
time.sleep(100)  """

# DAY - 4

"""XPATH AXES  - travels from top to bottom and bottom to top

self          - 
->whichever node we start from
-> SYNTAX - //*[attribute=’value’]/self::tagname

parent
-> traverse parent element of the current html tag
-> //*[attribute=’value’]/parent::parent::tagname

child
-> traverse all child elements of the current html tag.
-> SYNTAX - //*[attribute=’value’]/child::tagname

ancestor
-> Traverse all the ancestor elements(grandparent,parent etc ) of the current html tag
-> SYNTAX - //*[attribute=’value’]/ancestor::tagname

descendant
-> Traverse all the ancestor elements(child, grandchild etc ) of the current html tag
-> SYNTAX - //*[attribute=’value’]/descendant::tagname

following

->traverse all element that comes after the  current html tag.
-> SYNTAX - //*[attribute=’value’]/following::tagname

following-sibling
-> Traverse from current html tag to next sibling html tag
-> //current html tag[@attribute=’value’]/following-sibling::sibling tag [@attribute=’value’]

preceding
-> traverse all nodes that comes before the current html tag.
-> SYNTAX - //*[attribute=’value’]/preceding::tagname

preceding-sibling
-> Traverse from current html tag to previous sibling html tag
-> //current html tag[@attribute=’value’]/preceding-sibling::previous tag [@attribute=’value’]



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.implicitly_wait(20)

# self

#text_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Angel One']/self::a").text
#print(text_msg)

#parent


#p_msg=driver.find_element(By.XPATH, "//a[normalize-space()='Angel One']/parent::td").text
#print(p_msg)

#child
# our self element not have child so we go to ancestor and pick that child element

child=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/child::td")
print(len(child)) # return all the elements to that td category

#ancestor
# child element data will show
ar=driver.find_element(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr")
print(ar)

#descendant

des=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/descendant::*")
print(len(des))  #td-5 is descendnt of tr

#following(below ele)

fol=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/following::*")
print(len(fol))

#following sibling   (subset of following)
#we dont have siblings for self so we go the ancestor and find siblings
fol_sib=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/following-sibling::*")
print(len(fol_sib))

#preceding(above ele)

pre=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/preceding::tr")
print(len(pre))

#preceding siblings

pre_sib=driver.find_elements(By.XPATH, "//a[normalize-space()='Angel One']/ancestor::tr/preceding-sibling::tr")
print(len(pre_sib))


driver.quit()
time.sleep(100)
"""


# DAY - 5
"""
1.application commands
2.conditional commands
3.browser commands
4.navigational commands
5.wait commands


application commands
get - opening the app URL
title - to capture the title of current webpage
current_url - capture current_url of the web page
page_source - capture source code of the page

application elements done by driver

conditional commands 
is_displayed   - element is present in the webpage or not   
is_enabled     - element is enabled(element do some action) returns true.
is_selected    - check radio and checkboxes is selected returns true or false

conditional elements done by web_elements

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

BROWER COMMANDS

Close()  -  simply close the browser but backend process is running , close one browser at a time
Quit()  -  close browser along with process . close all the browsers


navigational commands
back
forward
refresh





driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
print(driver.page_source)


driver.quit()   """


"""driver.get("https://demo.nopcommerce.com/register")
search=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display status:",search.is_displayed())
print("enabled status:",search.is_enabled())

#is_selected for radio and checkbox

rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")
rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")

rd_female.click()
print(rd_female.is_selected())
print(rd_male.is_selected())

time.sleep(100)
driver.quit()


#navigational commands

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.get("https://www.amazom.com")

driver.back()   #back to orange app
driver.forward()   # go to amazon
driver.refresh()   #refresh the page
time.sleep(10)
driver.quit()  


driver.get("https://demo.nopcommerce.com/")
#find element -- matching with one ele

element_var=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
element_var.send_keys("Apple Phone")

#locaters matching with the multiple web elements

element_var=driver.find_element(By.XPATH,"//div[@class='footer']//a")
print(element.text)   # only print one web element because of find_element

#element not available them throw NosuchElementException
#find element is not able to find the element at that time it shows NosuchElementException

login=driver.find_element(By.LINK_TEXT,"Log")  #Log in is correct
login.click()



time.sleep(10)
driver.quit()   

######## find_elements() ##### - Return multiple webelements

# Locators match with single webelement

#elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
#print(len(elements)) #list collection we cannot able to access elements
#print(elements[0].send_keys())  # we extract web elements and send actions

# locators matching with multiple web elements
driver.get("https://demo.nopcommerce.com/")
element_var=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
print(len(element_var))

for ele in element_var:
    print(ele.text)


#element not avaliable
ele=driver.find_elements(By.LINK_TEXT,"Log")
print(len(ele))  # not show any exception

time.sleep(10)
driver.quit() 

######text vs get_attribute(values)#####

driver.get("https://demo.nopcommerce.com/")
email=driver.find_element(By.XPATH,"//input[@id-'Email']")
email.clear()  # default email is cleared
email.send_keys("abc@gmail.com")
print("result of text",email.text)   # Print nothing
print("result of get_attribute",email.get_attribute('value'))

#<input id="123"  name="xyz" > Email:</input>  .... Email is inner text
# Text - returns Inner text of the element
#get_attribute - returns values of any attribute of web element

log=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result of text",log.text)
print("result of get_attribute",log.get_attribute('value'))
print("result of get_attribute",log.get_attribute('type')) """


####### DAY -6 ########

# Wait commands - used for syrnchronizing prblm

"""


time.sleep (maximum time wait for that element)
advantage 
--- simple to use
Disadvantage
--- performance of the script is very poor
--- if the element is not available within the time mentioned still there is a chance of getting exception 

1.implicit wait(wait for element if element is available procedd to next)

ADVANTAGE

--- Single statement
--- performance will not be reduced (if the element is available within the time it proceed to execute further
DISADVANTAGE
-- If the element is not available within the time mentioned , still there is a chance of getting exception

# Amount of time driver should wait to find the element(if you call next condition it perform
# implicitly_wait - - it is applicable to all the below statements


2.explicit wait

explicit waits - it works based on condition
mywait=WebDriverWait(driver,10,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementsNotSelectableException,Exception])
poll_frequency=2  - total 10 sec in tha every 2 sec it goes and try to find that element it reduce time
mywait=WebDriverWait(driver,10,poll_frequency,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementsNotSelectableException,Exception])

Adv
-- More effectively work

Dis 

--  Multiple places enter feels some difficulty




import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
mywait=WebDriverWait(driver,10)  # explicit wait declaration



#driver.implicitly_wait(20)
driver.get("https://www.google.com/")
searchbox=driver.find_element(By.NAME,'q')
searchbox.send_keys("Selenium")
#searchbox.submit()    # Press enter key

#driver.find_element(By.XPATH,"//span[normalize-space()='selenium']").click()
#driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
mywait.click()# condition is stastified it will execute
#If the condition is not true until it wait for that element
time.sleep(10)
driver.quit() """


####DAY - 7 #######

"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Select checkboxes

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://itera-qa.azurewebsites.net/home/automation")
#driver.find_element(By.XPATH,"//input[@id='monday']").click()


checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@Id,'day')]")
print(len(checkboxes))


#for i in range(len(checkboxes)):
    #checkboxes[i].click()

#for checkbox in checkboxes:
    #checkbox.click()

# Select multiple
for checkbox in checkboxes:
    weekname=checkbox.get_attribute('id')
    if weekname=="monday" or weekname=="sunday":
        checkbox.click()

#Select two checkboxes from last

for i in range(len(checkboxes)-2,len(checkboxes)):  #Total 7 [range(5,7)]
    checkboxes[i].click()   # sat and sun

time.sleep(10)
driver.quit()


# select first 2 checkboxes

for i in range(2):
    checkboxes[i].click()
#or
for i in range(len(checkboxes)):
    if i<2:
        checkboxes[i].click()

#for select and unselect using the same click fun


#if selected remove that if unselected add that

for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
    else:
        checkbox.click()



######   LINKS   ###

1.Internal link   - Link available on same page
2.External link   - link navigate to other webpage
3.Broken link    - Target link is not available"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://demo.nopcommerce.com/")
driver.implicitly_wait(20)
driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()


links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))

for link in links:
    print(link.text)  # link is web element we cannot directly print so that we use text
time.sleep(100)
driver.quit()






