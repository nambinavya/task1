# learning_python.py

# 1. Variables and Data Types
a = 5
b = 3
text = "Hello, World!"
pi = 3.14
is_valid = True

print("Variables and Data Types:")
print("a =", a)
print("b =", b)
print("text =", text)
print("pi =", pi)
print("is_valid =", is_valid)
print()

# 2. Arithmetic Operations
sum = a + b
difference = a - b
product = a * b
quotient = a / b
modulus = a % b

print("Arithmetic Operations:")
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Modulus:", modulus)
print()

# 3. String Manipulation
print("String Manipulation:")
print(text.lower())  # Convert to lowercase
print(text.upper())  # Convert to uppercase
print(text.replace("World", "Python"))  # Replace substring
print()

# 4. Conditional Statements
num = 10
print("Conditional Statements:")
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
print()

# 5. Loops
print("Loops:")
print("For loop:")
for i in range(5):
    print(i)

print("While loop:")
count = 0
while count < 5:
    print(count)
    count += 1
print()

# 6. Functions
def greet(name):
    return f"Hello, {name}!"

print("Functions:")
print(greet("Alice"))
print()

# 7. Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Lists:")
print(fruits)
print(fruits[1])
print()

# 8. Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Dictionaries:")
print(person["name"])
person["age"] = 31
print(person)
print()

# 9. Tuples
colors = ("red", "green", "blue")
print("Tuples:")
print(colors[0])
print()

# 10. Combining Data Structures
def summarize_person(person):
    return f"{person['name']} is {person['age']} years old and lives in {person['city']}."

print("Combining Data Structures:")
person_summary = summarize_person(person)
print(person_summary)
print()

# Practice Examples

# Example: Check if a number is even or odd
def is_even(number):
    return number % 2 == 0

print("Check if a number is even or odd:")
number = 7
print(f"{number} is even: {is_even(number)}")
print()

# Example: Sum of elements in a list
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

print("Sum of elements in a list:")
numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers} is {sum_of_list(numbers)}")
print()

# Example: Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

print("Check if a string is a palindrome:")
word = "radar"
print(f"'{word}' is a palindrome: {is_palindrome(word)}")
