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

