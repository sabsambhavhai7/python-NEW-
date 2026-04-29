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

ques 5
from itertools import groupby
data = "AAABBBCCDAA"
compressed = "".join(f"{len(list(g))}{k}" for k, g in groupby(data))
print(f"Compressed: {compressed}") # 3A3B2C1D2A



ques 6
import inspect
def sample_func(a, b, c=10): pass

params = inspect.signature(sample_func).parameters
print(f"Function arguments: {list(params.keys())}")


ques 7
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

counter = count_up_to(5)
print(list(counter))



ques 8 
from itertools import chain
list_a = [1, 2]
list_b = ['a', 'b']
for item in chain(list_a, list_b):
    print(item, end=" ")


ques 9 
def lerp(start, end, t):
    return start + t * (end - start)

# Find value 25% of the way between 10 and 20
print(f"25% between 10 and 20: {lerp(10, 20, 0.25)}")



ques 10
data = [1, 2, 3, 4, 5]
data.clear()
print(f"List after clear: {data}")






















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

ques 10 
text = "Python is Fun"
print(text.swapcase()) # pYTHON IS fUN



 _________________________________________________________________________________________________________________________________________________


date - 9 april 2026

ques 1
def is_unique(lst):
    return len(lst) == len(set(lst))

nums = [1, 2, 3, 4, 5]
print(f"Are all unique? {is_unique(nums)}")

ques 2 
points = [(1, 2), (3, 4), (5, 6)]
flat = [num for t in points for num in t]
print(f"Flattened: {flat}")

ques 3
items = [10, 20, 30]
# Use pop() to get and remove, or just index -1 to peek
print(f"Last item: {items[-1] if items else 'Empty'}")

ques 4
users = [{"name": "Zoe", "age": 25}, {"name": "Alex", "age": 30}]
users.sort(key=lambda x: x["name"])
print(f"Sorted by name: {users}")

ques 5
import itertools
for i in itertools.count(start=10, step=5):
    if i > 30: break
    print(i, end=" ") # 10 15 20 25 30

ques 6
list1 = [1, 2, 3, 4]
list2 = [1, 2]
diff = list(set(list1) - set(list2))
print(f"Difference: {diff}")


ques 7 
from itertools import zip_longest
names = ["Alice", "Bob"]
scores = [100, 90, 80]
paired = list(zip_longest(names, scores, fillvalue="N/A"))
print(paired)

ques 8 
text = "apple banana apple cherry banana apple"
words = text.split()
freq = {word: words.count(word) for word in set(words)}
print(f"Word frequencies: {freq}")

ques 9 
# Standard range only does ints; this is a float-friendly generator
def float_range(start, stop, step):
    while start < stop:
        yield round(start, 2)
        start += step

print(list(float_range(0, 1, 0.2)))

ques 10 
list1 = [1, 2, 3, 4]
list2 = [1, 2]
diff = list(set(list1) - set(list2))
print(f"Difference: {diff}")





_________________________________________________________________________________________________________________________________________________


Date - 10 April 2026

ques 1 
import heapq
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = list(heapq.merge(list1, list2))
print(f"Merged sorted list: {merged}")


ques 2
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

p = Product("Laptop", 1200.00, 3)
print(p)

ques 3
old_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {value: key for key, value in old_dict.items()}
print(f"Swapped: {new_dict}")

ques 4
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"Is A a subset of B? {set_a.issubset(set_b)}")

ques 5
from itertools import groupby
data = "AAABBBCCDAA"
compressed = "".join(f"{len(list(g))}{k}" for k, g in groupby(data))
print(f"Compressed: {compressed}") # 3A3B2C1D2A


ques 6
import inspect
def sample_func(a, b, c=10): pass

params = inspect.signature(sample_func).parameters
print(f"Function arguments: {list(params.keys())}")

ques 7
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

counter = count_up_to(5)
print(list(counter))

ques 8 
from itertools import chain
list_a = [1, 2]
list_b = ['a', 'b']
for item in chain(list_a, list_b):
    print(item, end=" ")


ques 9 
def lerp(start, end, t):
    return start + t * (end - start)

# Find value 25% of the way between 10 and 20
print(f"25% between 10 and 20: {lerp(10, 20, 0.25)}")

ques 10
data = [1, 2, 3, 4, 5]
data.clear()
print(f"List after clear: {data}")




_________________________________________________________________________________________________________________________________________________


date - 11 april 2026 

ques 1 
import math
def round_sig(x, sig):
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)

print(round_sig(0.00123456, 3)) # 0.00123

ques 2
import heapq
pq = []
heapq.heappush(pq, (2, "Task B"))
heapq.heappush(pq, (1, "Task A")) # Lower number = higher priority
print(f"Next task: {heapq.heappop(pq)[1]}")


ques 3 
import re
def is_hex_color(code):
    return bool(re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', code))

print(is_hex_color("#FFA500")) # True


ques 4
def to_camel_case(text):
    words = text.split('_')
    return words[0] + ''.join(w.title() for w in words[1:])

print(to_camel_case("user_profile_data")) # userProfileData



ques 5
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# Elements in either set, but not both
print(f"Unique to each: {set1 ^ set2}")


ques 6
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")
print("Process continued without crashing.")

ques 7
from collections import Counter
data = [1, 2, 3, 1, 2, 1, 1, 4]
most_common_val, count = Counter(data).most_common(1)[0]
print(f"Value {most_common_val} appears {count} times.")


ques 8
import base64
text = "Python101"
encoded = base64.b64encode(text.encode())
print(f"Encoded: {encoded.decode()}")

ques 9
import base64
text = "Python101"
encoded = base64.b64encode(text.encode())
print(f"Encoded: {encoded.decode()}")


ques 10
import math
# Filters out private attributes starting with underscore
public_math = [attr for attr in dir(math) if not attr.startswith("_")]
print(f"First 5 math functions: {public_math[:5]}")


_________________________________________________________________________________________________________________________________________________

date - 12 april 2026

ques 1 
email = "user@example.com"
domain = email.split('@')[-1]
print(f"Domain: {domain}")

ques 2
# Returns a tuple of (quotient, remainder)
q, r = divmod(17, 5)
print(f"Quotient: {q}, Remainder: {r}")


ques 3
# An isogram is a word with no repeating letters
def is_isogram(word):
    return len(word.lower()) == len(set(word.lower()))

print(f"Is 'Python' an isogram? {is_isogram('Python')}")

ques 4
from itertools import groupby
data = [("Animal", "Dog"), ("Animal", "Cat"), ("Plant", "Oak")]
for key, group in groupby(data, lambda x: x[0]):
    print(f"{key}: {list(group)}")

ques 5
text = " P y t h o n   "
clean_text = "".join(text.split())
print(f"Cleaned: '{clean_text}'")

ques 6
def binary_search(arr, target, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    elif arr[mid] > target: return binary_search(arr, target, low, mid - 1)
    else: return binary_search(arr, target, mid + 1, high)

print(f"Index of 7: {binary_search([1, 3, 5, 7, 9], 7, 0, 4)}")

ques 7
nested = {'a': {'x': 1}, 'b': {'y': 2}}
flat = [(k, sub_k, v) for k, sub in nested.items() for sub_k, v in sub.items()]
print(flat)

ques 8 
class A: pass
class B(A): pass
print(f"Inheritance order for B: {B.mro()}")

ques 9 
from datetime import datetime, timedelta
start = datetime(2026, 4, 1)
date_list = [start + timedelta(days=x) for x in range(5)]
print([d.strftime("%Y-%m-%d") for d in date_list])


ques 10 
import sys
# Useful for terminating scripts on critical errors
if len(sys.argv) < 1:
    sys.exit("Error: No arguments provided.")
print("Script proceeding...") 



_________________________________________________________________________________________________________________________________________________

date - 13 april 2026

ques 1 
words = ["apple", "pie", "banana", "kiwi"]
words.sort(key=len)
print(f"Sorted by length: {words}")

ques 2
# Check if any number in the list is greater than 100
nums = [10, 55, 30, 105, 2]
has_large_num = any(x > 100 for x in nums)
print(f"Contains number > 100: {has_large_num}")

ques 3
# The "old school" way, still useful in some logging scenarios
name = "Gemini"
version = 3
print("Hello, %s version %d" % (name, version))

ques 4
stats = {'cpu': 20, 'memory': 80, 'disk': 15}
min_usage = min(stats, key=stats.get)
print(f"Lowest usage category: {min_usage}")

ques 5
import inspect
def demo_func():
    return "Hello"

# This prints the actual source code of the function
print(inspect.getsource(demo_func))


ques 6 
import inspect
def demo_func():
    return "Hello"

# This prints the actual source code of the function
print(inspect.getsource(demo_func))

ques 7
pairs = [('a', 1), ('b', 2), ('c', 3)]
result = dict(pairs)
print(result)


ques 8

import tempfile
with tempfile.TemporaryFile(mode='w+') as tf:
    tf.write('Secret data')
    tf.seek(0)
    print(f"Temp file content: {tf.read()}")
# File is automatically deleted here


ques 9
# Useful when dynamically creating variables or keys
print(f"Is 'var_1' valid? {'var_1'.isidentifier()}")
print(f"Is '1_var' valid? {'1_var'.isidentifier()}")


___________________________________________________________________________________________________________________________________________________

date - 14 april 2026


ques 1
grades = {"Math": 90, "Science": 85, "History": 88}
for i, (subject, score) in enumerate(grades.items(), start=1):
    print(f"{i}. {subject}: {score}")

ques 2
nums = [1, 5, 8, 12]
is_sorted = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
print(f"Is the list sorted? {is_sorted}")

ques 3
import re
text = "The price is 100 dollars and 50 cents."
numbers = re.findall(r'\d+', text)
print(f"Numbers found: {numbers}")

ques 4
from collections import defaultdict
data = {'a': 1, 'b': 2, 'c': 1}
rev_data = defaultdict(list)
for k, v in data.items():
    rev_data[v].append(k)
print(dict(rev_data)) # {1: ['a', 'c'], 2: ['b']}

ques 5
n = 98765
digits = [int(d) for d in str(n)]
print(f"Digits list: {digits}")

ques 6
import heapq
list_a = [1, 10, 20]
list_b = [5, 15, 25]
for val in heapq.merge(list_a, list_b):
    print(val, end=" ")

ques 7
keys = ['cpu', 'ram', 'gpu']
# Initializes all keys with 0
usage = dict.fromkeys(keys, 0)
print(usage)

ques 8
# Convert character to ASCII and vice-versa
char = 'A'
code = ord(char)
print(f"ASCII of {char} is {code}")
print(f"Character for 66 is {chr(66)}")

ques 9
import sys
data = {i: i**2 for i in range(1000)}
print(f"Memory size: {sys.getsizeof(data)} bytes")

ques 10
set_x = {1, 2, 3}
set_y = {4, 5, 6}
# Returns True if sets have no common elements
print(f"No overlap? {set_x.isdisjoint(set_y)}")


_________________________________________________________________________________________________________________________________________________

date 16 april , 2026

ques 1 
import statistics
data = [1, 3, 5, 7, 9, 11]
print(f"Median: {statistics.median(data)}")

ques 2
import textwrap
long_text = "Python is an interpreted, high-level, general-purpose programming language."
wrapped = textwrap.fill(long_text, width=30)
print(wrapped)

ques 3
def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(f"Is 'Listen' an anagram of 'Silent'? {is_anagram('Listen', 'Silent')}")


ques 4
# Note: Requires 'pip install tqdm'
# For the standard library version:
import time
for i in range(10):
    print(f"Processing... {i+1}/10", end="\r")
    time.sleep(0.3)

ques 5
def sieve(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
    return primes

print(f"Primes up to 50: {sieve(50)}")


ques 6
num = 42
formatted = str(num).zfill(5)
print(f"Padded ID: {formatted}") # 00042"

ques 7
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
common = set.intersection(*sets)
print(f"Common to all: {common}")


ques 8
from collections import Counter
data = ['A', 'A', 'B', 'C', 'A', 'B']
counts = Counter(data)
total = len(data)
percentages = {k: f"{(v/total)*100:.1f}%" for k, v in counts.items()}
print(percentages)

ques 9 
from itertools import permutations
items = ['A', 'B', 'C']
# Get all possible arrangements of 2 items
perms = list(permutations(items, 2))
print(f"Permutations: {perms}")


ques 10 
import os
print(f"Total CPU cores available: {os.cpu_count()}")


_________________________________________________________________________________________________________________________________________________

date 17 april 2026 

ques 1 
import sys
x = "Hello, Python!"
print(f"Memory size of string: {sys.getsizeof(x)} bytes")

ques 2
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 4]
diff = [item for item in list1 if item not in list2]
print(f"Difference: {diff}")

ques 3
from itertools import combinations
items = ['A', 'B', 'C', 'D']
# Find all unique pairs (order doesn't matter)
combos = list(combinations(items, 2))
print(f"Combinations: {combos}")

ques 4
def key_exists(data, key):
    if key in data: return True
    for v in data.values():
        if isinstance(v, dict):
            if key_exists(v, key): return True
    return False

nested = {'a': {'b': {'c': 10}}}
print(f"Does 'c' exist? {key_exists(nested, 'c')}")

ques 5
text = "Python"
byte_arr = bytearray(text, 'utf-8')
print(f"Byte Array: {byte_arr}")

ques 6
import bisect
sorted_list = [10, 20, 30, 40]
# Find where 25 should be inserted to keep the list sorted
bisect.insort(sorted_list, 25)
print(f"Updated list: {sorted_list}")

ques 7
hex_str = "0xFF"
val = int(hex_str, 16)
print(f"Decimal value: {val}")

ques 8
nums = [2, 4, 6, 8]
# Returns True only if every number is even
all_even = all(n % 2 == 0 for n in nums)
print(f"Are all even? {all_even}")

ques 9 
import shlex
cmd = 'echo "Hello World" --count 5'
parsed = shlex.split(cmd)
print(f"Parsed command: {parsed}")

ques 10 
import os
print(f"Running on Process ID: {os.getpid()}")


_________________________________________________________________________________________________________________________________________________

date 18 april 2026 

ques 1
import itertools
nums = [1, 2, 3, 4, 5]
cum_sum = list(itertools.accumulate(nums))
print(f"Cumulative Sum: {cum_sum}") # [1, 3, 6, 10, 15]

ques 2
import fnmatch
files = ["data1.txt", "data2.jpg", "config.ini", "data3.txt"]
txt_files = fnmatch.filter(files, "data*.txt")
print(f"Filtered files: {txt_files}")

ques 3
import inspect
def my_awesome_function():
    print(f"Executing: {inspect.stack()[0].function}")

ques 4
import os
folder = "logs_directory"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"Created {folder}")

my_awesome_function()


ques 4
from operator import itemgetter
users = [("Alice", 25), ("Bob", 19), ("Charlie", 30)]
# Sort by age (index 1) - faster than lambda for large datasets
users.sort(key=itemgetter(1))
print(f"Sorted by age: {users}")


ques 5
import re
text = "Hello, world! Welcome to Python."
words = re.findall(r'\w+', text)
print(f"Words: {words}")

ques 6
scores = {"Alice": 85, "Bob": 40, "Charlie": 92}
passed = {name: score for name, score in scores.items() if score >= 50}
print(f"Passed: {passed}")


ques 7
from itertools import chain
nested = [[1, 2], [3, 4], [5]]
flat = list(chain.from_iterable(nested))
print(f"Flattened: {flat}")


ques 8 
from datetime import datetime
t1 = datetime.now()
t2 = datetime(2026, 12, 31, 23, 59)
duration = t2 - t1
print(f"Seconds until New Year: {int(duration.total_seconds())}")

ques 9
# repr() shows the "official" string representation, including hidden chars
raw_str = "Line 1\nLine 2\tTabbed"
print(f"Normal: {raw_str}")
print(f"Debug: {repr(raw_str)}")

ques 10 
card_num = "1234567812345678"
masked = "*" * 12 + card_num[-4:]
print(f"Card: {masked}")


_________________________________________________________________________________________________________________________________________________


19 april 2026 

ques 1
class MySystem:
    def identify(self):
        return self.__class__.__name__

obj = MySystem()
print(f"Class Name: {obj.identify()}")

ques 2
seconds = 3665
minutes, sec = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
print(f"Time: {hours}h {minutes}m {sec}s")


ques 3
import string
alphabet = list(string.ascii_lowercase)
print(f"First 5 letters: {alphabet[:5]}")


ques 4
import random
deck = ["Ace", "King", "Queen", "Jack"]
random.shuffle(deck)
print(f"Shuffled: {deck}")

ques 5
import random
deck = ["Ace", "King", "Queen", "Jack"]
random.shuffle(deck)
print(f"Shuffled: {deck}")

ques 6
text = "hello"
# Check if the object has a 'upper' method
if hasattr(text, 'upper'):
    print(text.upper())

ques 7
text = "hello"
# Check if the object has a 'upper' method
if hasattr(text, 'upper'):
    print(text.upper())

ques 8
import itertools
# Get the first 3 items from a range without creating a full list
for i in itertools.islice(range(1000000), 3):
    print(f"Processing item: {i}")

ques 9 
val = "True"
bool_val = val == "True"
print(f"Boolean Type: {type(bool_val)} - Value: {bool_val}")

ques 10
text = "Python Programming"
vowels = "aeiou"
count = sum(1 for char in text.lower() if char in vowels)
print(f"Total Vowels: {count}")


_________________________________________________________________________________________________________________________________________________


20 th april 2026

ques 1
from collections import Counter
text = "success"
most_common = Counter(text).most_common(1)[0]
print(f"Most frequent char: '{most_common[0]}' ({most_common[1]} times)")

ques 2
# Adds elements of two lists together index by index
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(f"Summed lists: {result}")

ques 3
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

print(f"Is '12.5' a float? {is_float('12.5')}")

ques 4
class Config:
    port = 8080

c = Config()
# If 'host' doesn't exist, it returns 'localhost' instead of an error
host = getattr(c, 'host', 'localhost')
print(f"Connecting to: {host}")

ques 5
# range(start, stop, step)
evens = list(range(0, 21, 2))
print(f"Evens to 20: {evens}")

ques 6
items = ["apple", "banana", "cherry", "banana"]
if "banana" in items:
    items.remove("banana") # Removes only the first occurrence
print(f"Updated items: {items}")

ques 7
items = ["apple", "banana", "cherry", "banana"]
if "banana" in items:
    items.remove("banana") # Removes only the first occurrence
print(f"Updated items: {items}")

ques 8
import time
print(f"Current local time: {time.ctime()}")

ques 9
matrix = [[1, 2], [3, 4], [5, 6]]
transposed = [list(i) for i in zip(*matrix)]
print(f"Transposed Matrix: {transposed}")

ques 10
data = [10, 10, 10, 10]
all_same = len(set(data)) == 1
print(f"Are all elements identical? {all_same}")


_________________________________________________________________________________________________________________________________________________

date - 21 april 2026 



ques 2

ques 3

ques 4

ques 5

_________________________________________________________________________________________________________________________________________________

date 24 april 2026 

ques 1 
def deep_flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from deep_flatten(item)
        else:
            yield item

nested = [1, [2, [3, 4], 5], 6]
print(list(deep_flatten(nested))) # [1, 2, 3, 4, 5, 6]

ques 2
from collections import deque
queue = deque(["Task 1", "Task 2"])
queue.append("Task 3") # Add to right
queue.popleft()        # Remove from left (faster than list.pop(0))
print(f"Remaining: {list(queue)}")

ques 3
text = "python is amazing"
print(text.title()) # Python Is Amazing

ques 4
filename = "data_analysis.v2.csv"
extension = filename.rsplit('.', 1)[-1]
print(f"Extension: {extension}")

ques 5
votes = {"Red": 10, "Blue": 15, "Green": 8}
winner = max(votes, key=votes.get)
print(f"Winner: {winner}")

ques 6
miles = 10
km = miles * 1.60934
print(f"{miles} miles is {km:.2f} kilometers")

ques 7
shout = "HELLO WORLD"
print(f"Is uppercase? {shout.isupper()}")

ques 8 
dict_a = {'x': 1, 'y': 2, 'z': 3}
dict_b = {'w': 5, 'x': 10, 'y': 20}
common_keys = dict_a.keys() & dict_b.keys()
print(f"Keys in both: {common_keys}")

ques 9 
import itertools
# Creates an iterator that returns 'Hello' 3 times
for greeting in itertools.repeat("Hello", 3):
    print(greeting)

ques 10
# Returns True if any item is truthy (not 0, None, False, or empty)
data = [0, None, "", 42]
print(f"Does it have real data? {any(data)}") # True because of 42

_________________________________________________________________________________________________________________________________________________

Date 26 april 2026

ques 1


_________________________________________________________________________________________________________________________________________________

date 29 april 2026 

ques 1 
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with {args}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(5, 10)

ques 2 
# A generator function for Fibonacci sequence
def fib_gen(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Usage
for num in fib_gen(100):
    print(num, end=" ")

ques 3 
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    print(f"Initializing {name}...")
    yield f"Resource: {name}"
    print(f"Cleaning up {name}...")

with managed_resource("DataStream") as r:
    print(f"Using {r}")

ques 4 
users = [("Alice", 25), ("Bob", 17), ("Charlie", 30)]

# Create a dict of adults only
adult_map = {name: age for name, age in users if age >= 18}
print(adult_map) # {'Alice': 25, 'Charlie': 30}

ques 5
numbers = [1, 2, 3, 4, 5, 6]

# Square even numbers only
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares) # [4, 16, 36]

ques 6
from collections import defaultdict

groups = defaultdict(list)
data = [('tech', 'Python'), ('tech', 'Rust'), ('art', 'Sketching')]

for category, item in data:
    groups[category].append(item)

print(dict(groups)) # {'tech': ['Python', 'Rust'], 'art': ['Sketching']}


ques 7 
class Employee:
    raise_amt = 1.05
    
    def __init__(self, pay):
        self.pay = pay

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(day):
        return day.weekday() < 5 # Monday=0, Sunday=6
