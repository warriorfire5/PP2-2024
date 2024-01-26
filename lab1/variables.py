# Example 1 

x = 5
y = "John"
print(type(x))
print(type(y))

# Example 2

x = "John"
# is the same as
x = 'John'

# Example 3

a = 4
A = "Sally"
#A will not overwrite a

# Example 4
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example 5

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Example 6

x = y = z = "Orange"
print(x)
print(y)
print(z)

# Example 7

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Example 8
x = "Python is awesome"
print(x)

# Example 9

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Example 10

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 11

x = 5
y = 10
print(x + y)

# Example 12

x = 5
y = "John"
print(x + y)

# Example 13

x = 5
y = "John"
print(x, y)

# Example 14

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Example 15

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Example 16

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Example 17

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)