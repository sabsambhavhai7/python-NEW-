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


___________________________________________________________________________________________________________________________________________________


Date: April 1, 2026

ques 1
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(f"Flattened list: {flat_list}")

ques 2
fruits = ["Apple", "Banana", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"Rank {index}: {fruit}")

ques 3
from collections import Counter
text = "abracadabra"
counts = Counter(text)
print(f"Character counts: {dict(counts)}")

ques 4
a, b = 5, 10
a, b = b, a
print(f"a: {a}, b: {b}")

ques 5
import sys
large_list = list(range(10000))
print(f"Memory size: {sys.getsizeof(large_list)} bytes")

ques 6 
import string
import random
chars = string.ascii_letters + string.digits
password = ''.join(random.choice(chars) for i in range(8))
print(f"Generated Password: {password}")

ques 7
str_nums = ["1", "2", "3", "4"]
int_nums = list(map(int, str_nums))
print(f"Converted integers: {int_nums}")

ques 8 
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Combined unique set: {union_set}")

ques 9
import os
print(f"Current Directory: {os.getcwd()}")

ques 10
import json
json_data = '{"name": "Kevin", "age": 30, "city": "Chicago"}'
parsed = json.loads(json_data)
print(f"Name from JSON: {parsed['name']}")


_________________________________________________________________________________________________________________________________________________


Date: April 2, 2026

ques 1
import copy
original = [[1, 2, 3], [4, 5, 6]]
# Deep copy creates a completely independent clone of nested objects
deep_clone = copy.deepcopy(original)
deep_clone[0][0] = 99
print(f"Original: {original[0][0]} | Deep Clone: {deep_clone[0][0]}")

ques 2
import copy
original = [[1, 2, 3], [4, 5, 6]]
# Deep copy creates a completely independent clone of nested objects
deep_clone = copy.deepcopy(original)
deep_clone[0][0] = 99
print(f"Original: {original[0][0]} | Deep Clone: {deep_clone[0][0]}")

ques 3
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common = list(set(list_a) & set(list_b))
print(f"Common elements: {common}")

ques 4
results = [True, False, True]
print(f"Is at least one True? {any(results)}")
print(f"Are all True? {all(results)}")

ques 5
import time
start_time = time.time()
# Simulate a task
time.sleep(0.5)
end_time = time.time()
print(f"Execution time: {end_time - start_time:.4f} seconds")

ques 6
import string
text = "Hello, World! How's it going?"
clean_text = text.translate(str.maketrans('', '', string.punctuation))
print(clean_text)

ques 7
for i in range(1, 11):
    progress = "[" + "=" * i + " " * (10 - i) + "]"
    print(f"\rLoading {progress} {i*10}%", end="")
    time.sleep(0.1)

ques 8
data = [1, 3, 3, 2, 1, 3, 4, 3, 2]
most_common = max(set(data), key=data.count)
print(f"Most frequent item: {most_common}")

ques  9 
from collections import defaultdict
counts = defaultdict(int) # Default value for new keys is 0
counts["apples"] += 1
print(f"Apples: {counts['apples']}, Oranges: {counts['oranges']}")

ques 10 
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)

ques 11
user_input = "12345"
if user_input.isdigit():
    print("Valid numeric input")
else:
    print("Contains non-digit characters")


___________________________________________________________________________________________________________________________________________________


date - 4 april 2026

ques 1
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Coordinates: x={p.x}, y={p.y}")


ques 2
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = [x for x in list1 if x in list2]
print(f"Intersection: {intersection}")

ques 3
import datetime
today = datetime.date.today()
print(f"Today is a: {today.strftime('%A')}")


ques 4
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")


ques 5
import urllib.request
with urllib.request.urlopen('https://www.google.com') as response:
   print(f"Status Code: {response.getcode()}")

ques 6
prices = {'apple': 0.5, 'orange': 0.3, 'banana': 0.2}
sorted_prices = dict(sorted(prices.items(), key=lambda item: item[1]))
print(f"Sorted by price: {sorted_prices}")


ques 7
data = [1, 2, 3]
if isinstance(data, list):
    print("This is a list!")

ques 8
from datetime import date
d1 = date(2026, 1, 1)
d2 = date(2026, 4, 4)
delta = d2 - d1
print(f"Days passed: {delta.days}")

ques 9 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Keep only the first 5 elements
del nums[5:]
print(f"Truncated list: {nums}")

ques 10
class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass()
attr_name = "value"
print(f"Dynamic value: {getattr(obj, attr_name)}")


_________________________________________________________________________________________________________________________________________________

Date - 6 april 2026

ques 1 
import itertools
colors = itertools.cycle(['Red', 'Green', 'Blue'])
# Prints the next three items in the cycle
print(next(colors), next(colors), next(colors), next(colors))

ques 2
matrix = [[1, 2], [3, 4], [5, 6]]
transpose = [list(row) for row in zip(*matrix)]
print(f"Transposed: {transpose}")


ques 3
import os
path = os.getenv("PATH")
print(f"First 50 chars of PATH: {path[:50]}...")

ques 4
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten([1, [2, [3, 4], 5]]))

ques 5
number = 255
print(f"Binary: {bin(number)}, Octal: {oct(number)}, Hex: {hex(number)}")


ques 6
number = 255
print(f"Binary: {bin(number)}, Octal: {oct(number)}, Hex: {hex(number)}")

ques 7
data = [1, 5, 2, 1, 9, 2, 10]
unique_ordered = list(dict.fromkeys(data))
print(unique_ordered)


ques 8
import sys
print(f"Python version: {sys.version.split()[0]}")


ques 9
def round_to_nearest(n, m):
    return m * round(n / m)

print(round_to_nearest(37, 10)) # Rounds to 40


ques 10
def future_function():
    # Placeholder to prevent indentation errors until code is written
    pass

print("Function defined successfully with 'pass'")


_________________________________________________________________________________________________________________________________________________

date - 7 april 2026

ques 1 
fruits = ["apple", "banana", "cherry"]
for fruit in reversed(fruits):
    print(fruit)

ques 2
filename = "report.pdf"
if filename.endswith(".pdf"):
    print("This is a PDF document.")


ques 3
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

nums = [1, 2, 3, 4, 5]
print(f"Rotated by 2: {rotate_list(nums, 2)}")

ques 4
# Removes all "falsy" values (0, False, None, empty strings)
data = [0, 1, False, 2, '', 3, None]
filtered_data = list(filter(None, data))
print(f"Cleaned data: {filtered_data}")

ques 5
# Removes all "falsy" values (0, False, None, empty strings)
data = [0, 1, False, 2, '', 3, None]
filtered_data = list(filter(None, data))
print(f"Cleaned data: {filtered_data}")

ques 6
import math
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")

ques 7
import heapq
scores = [55, 89, 76, 99, 100, 45]
print(f"Top 3 scores: {heapq.nlargest(3, scores)}")

ques 8
phrase = "The quick brown fox"
if "brown" in phrase:
    print("Found 'brown' in the string!")

ques 9
raw_name = "john doe smith"
print(raw_name.title()) # Output: John Doe Smith

ques 10
import os
# Replace 'test.txt' with an actual filename to test
try:
    size = os.path.getsize('test.txt')
    print(f"File size: {size} bytes")
except FileNotFoundError:
    print("File not found.")


_________________________________________________________________________________________________________________________________________________

Date- 8 APRIL 2026

ques 1
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

ques 2
multiline = (
    "This is a way to write "
    "a very long string without "
    "using triple quotes."
)
print(multiline)

ques 3
class Person:
    def __init__(self):
        self.name = "Leo"
        self.age = 30

p = Person()
print(vars(p)) # Returns a dictionary of attributes

ques 4
nums = [10, 50, 20, 100, 5]
max_index = nums.index(max(nums))
print(f"Max value is at index: {max_index}")

ques 5
separator = "-" * 20
print(separator)
print("Centered Text")
print(separator)


ques 6
a = [1, 2, 3]
b = [2, 3, 4]
intersection = list(set(a).intersection(b))
print(f"Shared elements: {intersection}")

ques 7
import uuid
unique_id = uuid.uuid4()
print(f"Generated UUID: {unique_id}")



ques 8
import glob
# Finds all Python files in the current directory
py_files = glob.glob("*.py")
print(f"Python files found: {py_files}")

ques 9
items = [{"price": 10}, {"price": 20}, {"price": 15}]
total = sum(item["price"] for item in items)
print(f"Total Price: {total}")



 






