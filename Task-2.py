""" TASK - 2"""

#QUESTION-1
Given a python list [10, 501, 22, 37, 100, 999, 87, 351] your task is to create two listone which have all the even numbers and another list which have all ODD numbers

list1 = [10, 501, 22, 37, 100, 999, 87, 351]
even_list = []
odd_list = []

for num in list1:
  if num % 2 == 0:
    even_list.append(num)
  else:
    odd_list.append(num)

print("Even list:", even_list)
print("Odd list:", odd_list)

"""OUTPUT
Even list: [10, 22, 100]
Odd list: [501, 37, 999, 87, 351]
"""


# 2

def is_prime(n):
  if n <= 1:           # 0 then negative values not included in prime
    return False
  for i in range(2, int(n**0.5) + 1):         # n**0.5 to take the square root (2,3.1+1)=(2,4)
    if n % i == 0:          #10/3!=0  so 10 is not prime
      return False
  return True

list1 = [10, 501, 22, 37, 100, 999, 87, 351]
prime_numbers = [num for num in list1 if is_prime(num)]

print(f'prime numbers is {prime_numbers}')

"""OUTPUT
prime numbers is [37]
"""

#3
"""“happy” is a number which sum of its squared digits will eventually be 1, after infinite number of iterations"""

def is_happy_number(n):
  seen = set()
  while n != 1 and n not in seen:          #This loop continues until either n becomes 1
    seen.add(n)         # it take only non happy numbers
    sum_of_squares = 0
    while n > 0:
      remainder = n % 10
      sum_of_squares = sum_of_squares + remainder * remainder
      n //= 10
    n = sum_of_squares
  return n == 1

list1 = [10, 501, 22, 37, 100, 999, 87, 351]

happy_numbers = sum(is_happy_number(num) for num in list1)
print(f'happy numbers is {happy_numbers}'')

"""OUTPUT
happy numbers is 2
"""

#4

def sum_first_last_digit(number):
    num_str = str(number)
    first_digit = int(num_str[0])          # take 1st num
    last_digit = int(num_str[-1])          # take last num
    sum_digits = first_digit + last_digit   # add both 1st and last
    return sum_digits
number = int(input("Enter an integer: "))  # Input the integer
result = sum_first_last_digit(number)  # Calculate the sum of first and last digits
print("Sum of first and last digit:", result)  # Print the result

"""OUTPUT
Sum of first and last digit: 8
"""

#5

def distribute_mangoes(mangoes, students):
  mangoes.sort(reverse=True)
  student_mangoes = [0] * students
  for i in range(len(mangoes)):
    student_mangoes[i % students] += mangoes[i]
  return max(student_mangoes) - min(student_mangoes)
mangoes = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
students = 5

difference = distribute_mangoes(mangoes, students)

print(f'difference is {difference}')

"""OUTPUT

difference is 8
"""


#6

def merge_lists(list1, list2, list3):
    merged_list = list1 + list2 + list3
    unique_elements = list(set(merged_list))      # set not allow duplicates
    return unique_elements

result = merge_lists([1, 2, 3], [3, 4, 5], [5, 6, 7, 8])
print(result)

"""OUTPUT
[1, 2, 3, 4, 5, 6, 7, 8]
"""

#7

def first_non_repeating_number(list1):
  seen = set()
  for number in list1:
    if number not in seen:
      return number
    seen.add(number)
  return -1

list1 = [1, 2, 3, 4, 5, 1, 2, 3]
first_non_repeating_number = first_non_repeating_number(list1)
print(f'first_non_repeating_number is {first_non_repeating_number}')

"""OUTPUT
first_non_repeating_number is 1
"""

#QUESTION- 8

# Sorted list (ascending order)
sorted_list = [1, 3, 5, 7, 9, 11, 13]

# Find the minimum element (first element in the sorted list)
minimum_element = sorted_list[0]

print("Minimum element in the list is:", minimum_element)

"""OUTPUT
Minimum element in the list is: 1
"""

"""or"""
def find_min_element(list1):
  return list1[0]
list1 = [1, 5, 10, 15, 20]
min_element = find_min_element(list1)
print(f'min element is {min_element}'')

"""OUTPUT
min element is 1
"""

#QUESTION- 9

numbers = [10, 20, 30, 9]
target_sum = 59

# Find triplets with given sum
triplets = [(a, b, c) for a in numbers for b in numbers for c in numbers if a + b + c == target_sum and a != b and b != c and a != c]

# Print the result
if triplets:
    print("Triplets with sum", target_sum, "are:")
    print(triplets)
else:
    print("No triplets found with the given sum.")

"""OUTPUT
Triplets with sum 59 are:
[(20, 30, 9), (20, 9, 30), (30, 20, 9), (30, 9, 20), (9, 20, 30), (9, 30, 20)]
"""


#10
def find_sublist_with_sum_zero(list1):
  cumulative_sums = set()
  current_sum = 0
  for element in list1:
    current_sum += element
    if current_sum == 0 or current_sum in cumulative_sums:
      return True
    cumulative_sums.add(current_sum)
  return False
list1 = [4, 2, -3, 1, 6]
result = find_sublist_with_sum_zero(list1)
print(result)

"""OUTPUT
True
"""

 #another method

def has_sublist_with_zero_sum(nums):
    prefix_sum = 0
    seen_sums = set()
    for num in nums:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen_sums:
            return True
        seen_sums.add(prefix_sum)
    return False
my_list = [4, 2, -3, 1, 6]
if has_sublist_with_zero_sum(my_list):
    print("Yes, there is a sublist with a sum equal to zero.")
else:
    print("No, there is no sublist with a sum equal to zero.")

"""OUTPUT
Yes, there is a sublist with a sum equal to zero.
"""