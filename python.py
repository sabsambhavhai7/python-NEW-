Date: March 28, 2026
 ques 1
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print(is_prime(29))

ques 2 
text = "Python Programming"
reversed_text = text[::-1]
print(reversed_text)

ques 3 
import random
print(random.randint(1, 100))

ques 4
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

ques 5
student = {"name": "Leo", "age": 22, "major": "CS"}
print(len(student))

ques 6
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")

ques 7
grades = [88, 92, 79, 95, 84]
print(max(grades))

ques 8 
import time
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Blast off!")

ques 9
word = "radar"
is_palindrome = word == word[::-1]
print(f"Is {word} a palindrome? {is_palindrome}")

ques 10
import math
num = 64
print(math.sqrt(num))

_________________________________________________________________________________________________________________________________________________

Date: March 29, 2026



QUES 1
items = [1, 2, 2, 3, 4, 4, 4, 5]
unique_items = list(set(items))
print(f"Original: {items} | Unique: {unique_items}")

QUES 2
keys = ["Name", "Age", "City"]
values = ["Sophia", 28, "Berlin"]
user_dict = dict(zip(keys, values))
print(user_dict)

QUES 3 
import math
num = 5
print(f"The factorial of {num} is {math.factorial(num)}")

QUES 4
colors = ["red", "blue", "red", "green", "red", "blue"]
count_red = colors.count("red")
print(f"Red appears {count_red} times.")

QUES 5
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Buddy")
print(my_dog.bark())

QUES 6
scores = [80, 90, 70, 100]
average = sum(scores) / len(scores)
print(f"Average score: {average}")

QUES 7
numbers = list(range(10)) # 0 to 9
# Get every second number
print(f"Every second number: {numbers[::2]}")

QUES 8
import os
file_exists = os.path.isfile("data.csv")
print(f"Does the file exist? {file_exists}")

QUES 9 
def simple_decorator(func):
    def wrapper():
        print("Function is about to run...")
        func()
        print("Function has finished.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello World!")

say_hello()

QUES 10
data = [("Apple", 5), ("Banana", 2), ("Orange", 8)]
data.sort(key=lambda x: x[1])
print(f"Sorted by quantity: {data}")
