# Example 1
# Which takes the second letter in word HELLO
a = "Hello, World!"
print(a[1])

# Example 2

for x in "banana":
  print(x)

# Example 3
  
a = "Hello, World!"
print(len(a))

# Example 4

txt = "The best things in life are free!"
print("free" in txt)

# Example 5

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Example 6
  
txt = "The best things in life are free!"
print("expensive" not in txt)

# Example 7

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# Example 8
  
b = "Hello, World!"
print(b[2:5])

# Example 9

b = "Hello, World!"
print(b[:5])

# Example 10

b = "Hello, World!"
print(b[2:])

# Example 11

#Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])


# Example 12

a = "Hello, World!"
print(a.upper())

# Example 13

a = "Hello, World!"
print(a.lower())

# Example 14

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Example 15

a = "Hello, World!"
print(a.replace("H", "J"))

# Example 16

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# Example 17

a = "Hello"
b = "World"
c = a + b
print(c)

# Example 18

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Example 19

age = 36
txt = "My name is John, I am " + age
print(txt)

# Example 20

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# Example 21

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Example 22

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Example 23

txt = "We are the so-called \"Vikings\" from the north."
print ( txt ) 


