"""Shape	Area	Perimeter
Circle	A = π × r2	Circumference = 2πr"""

# OOPS CONCEPT
"""Create a python program called circle with constructor which will take a list an argument
From the given list create two class methods area and perimeter which will belong to calculate area and perimeter"""


"""class Circle:
    pi = 3.141

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = Circle.pi * radius * radius
        return area

    def perimeter(self):
        circumference = 2 * Circle.pi * self.radius
        return circumference


list = [10, 501, 22, 37, 100, 999, 87, 351]
for radius in list:
    circle_obj = Circle(radius)
    print(f"Radius: {radius}")
    print(f"Area: {circle_obj.area()}")
    print(f"Perimeter: {circle_obj.perimeter()}")
    print("------")  """



# TASK - 9

# Expected output

data =[10, 501, 22, 37, 100, 999, 87, 351]
result = filter(lambda x:x>4,data)
print(list(result))

# 2. Write a python code using lambda function to check every element of an list is interger or string

data = [10, 501, 22, 37, 100, 999, 87, 351]

# Lambda function to check if the element is an integer or a string
check_type = lambda x: "Integer" if isinstance(x, int) else "String"

# Using lambda function to check the type of each element in the list
for i in data:
    result = check_type(i)
    print(f"{i} is {result}")

#3 . using a python lambda function to create a fibonacci serious from 1 to 50 elements?
from functools import reduce

fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
								range(n-2), [0, 1])

print(fib(50))


def fibonacci(count):
   listA = [0, 1]
   any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))
   return listA[:count]
print(fibonacci(50))

# 4 write a python function to validate the regular expression for following
# EMAIL ADDRESS
def is_valid_email(email):
    if email.count('@') != 1:   # Counting '@' Symbol:
        return False
    local_part, domain_part = email.split('@')  #Splitting Local Part and Domain Part
    if not local_part or not domain_part:       #Checking Non-Empty Parts:
        return False
    domain, tld = domain_part.split('.')        #Splitting Domain and TLD(top level domain)
    if not domain or not tld:                   #Checking Non-Empty Domain and TLD
        return False
    return True
# Example usage
email1 = "user@example.com"
email2 = "invalid_email@.com"
email3 = "another.user@domain.co"
print(f"Is '{email1}' a valid email? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {is_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {is_valid_email(email3)}")

#OR
import re


def is_valid_email(email):
    # Regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


# Example usage
email1 = "user@example.com"
email2 = "invalid_email@.com"
email3 = "another.user@domain.co"
print(f"Is '{email1}' a valid email? {is_valid_email(email1)}")
print(f"Is '{email2}' a valid email? {is_valid_email(email2)}")
print(f"Is '{email3}' a valid email? {is_valid_email(email3)}")



# MOBILE NUMBER OF BANGLADESH
def is_valid_bangladeshi_mobile_number(number):
    # Remove spaces or dashes from the input number
    cleaned_number = number.replace(" ", "").replace("-", "")
# Check if the number starts with '+880' and has 11 digits after the prefix
    if cleaned_number.startswith("+880") and len(cleaned_number) == 14 and cleaned_number[4:].isdigit():
        return True
# Check if the number starts with '01' and has 11 digits after that
    if cleaned_number.startswith("01") and len(cleaned_number) == 11 and cleaned_number.isdigit():
        return True
# If neither condition is met, it's not a valid Bangladeshi mobile number
    return False
# Example usage
mobile_number1 = "+8801712345678"
mobile_number2 = "01987654321"
mobile_number3 = "+8801112345678"
print(f"Is '{mobile_number1}' a valid Bangladeshi mobile number? {is_valid_bangladeshi_mobile_number(mobile_number1)}")
print(f"Is '{mobile_number2}' a valid Bangladeshi mobile number? {is_valid_bangladeshi_mobile_number(mobile_number2)}")
print(f"Is '{mobile_number3}' a valid Bangladeshi mobile number? {is_valid_bangladeshi_mobile_number(mobile_number3)}")


# TELEPHONE NUMBER OF USA

class PhoneNumberValidator:
    def __init__(self, numbers):
        self.numbers = numbers

    def is_valid_us_phone_number(self, phone_number):
        cleaned_number = ''.join(filter(str.isdigit, phone_number))
        if len(cleaned_number) == 10 and cleaned_number[0] in '23456789':
            return True
        else:
            return False

    def validate_numbers(self):
        valid_numbers = []
        for number in self.numbers:
            if self.is_valid_us_phone_number(number):
                valid_numbers.append(number)
        return valid_numbers


# Example usage
phone_numbers = ["(123) 456-7890", "555-1234", "1234567890"]
validator = PhoneNumberValidator(phone_numbers)
valid_numbers = validator.validate_numbers()

print(f"Valid US phone numbers: {valid_numbers}")

"ORR"


def is_valid_us_phone_number(phone_number):
    # Remove all non-digit characters from the phone number
    cleaned_number = ''.join(filter(str.isdigit, phone_number))

    # Check if the cleaned number has 10 digits and starts with 2-9
    if len(cleaned_number) == 10 and cleaned_number[0] in '23456789':
        return True
    else:
        return False


# Example usage
phone_number1 = "(123) 456-7890"
phone_number2 = "555-1234"
phone_number3 = "1234567890"
print(f"Is '{phone_number1}' a valid US phone number? {is_valid_us_phone_number(phone_number1)}")
print(f"Is '{phone_number2}' a valid US phone number? {is_valid_us_phone_number(phone_number2)}")
print(f"Is '{phone_number3}' a valid US phone number? {is_valid_us_phone_number(phone_number3)}")


# 16 Characters alpha numeric password composed of alphabets of upper case , lower case , special characters , numbers.

def password(password):
    lowercase = any(char.islower() for char in password)
    uppercase = any(char.isupper() for char in password)
    digit = any(char.isdigit() for char in password)
    special_char = any(char in '!@#$%^&*()_+{}[]:;<>,.?~\\-/' for char in password)

    return lowercase and uppercase and digit and special_char and len(password) >= 8

password1 = "Abc@1234"
password2 = "Password123"

print(f"Is '{password1}' valid -  {password(password1)}")
print(f"Is '{password2}' valid - {password(password2)}")



"ORR"


def is_password(password):
# Define sets of characters for different types of characters
    lowercase_charts = set('abcdefghijklmnopqrstuvwxyz')
    uppercase_charts = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('0123456789')
    special_char = set('!@#$%^&*()_+{}\[\]:;<>,.?~\\/-')
# Initialize flags for different character types
    lowercase = False
    uppercase = False
    digit = False
    special = False
# Check each character in the password
    for char in password:
        if char in lowercase_charts:
            lowercase = True
        elif char in uppercase_charts:
            uppercase = True
        elif char in digits:
            digit = True
        elif char in special_char:
            special = True
# Check if all required character types are present and the length is at least 8 characters
    return lowercase and uppercase and digit and special and len(password) >= 8

password1 = "Abc@1234"
password2 = "Password123"


print(f"Is '{password1}'  valid - {is_password(password1)}")
print(f"Is '{password2}'  valid - {is_password(password2)}")





