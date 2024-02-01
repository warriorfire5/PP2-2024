#Example 1

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Example 2

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Example 3

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Example 4

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#Example 5

list1 = ["abc", 34, True, 40, "male"]

#Example 6

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#Example 7

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Example 8

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) 

#ans banana

#Example 9

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) 

#ans cherry

#Example 10

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#Example 11

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#This will return the items from index 0 to index 4.


#Example 12

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#This will return the items from index 2 to the end.

#Example 13

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Negative indexing means starting from the end of the list.


#Example 14

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  # Checks if the apple is in list 

#Example 15
  
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#changees['apple', 'blackcurrant', 'cherry']

#Example 16

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"

#Example 17

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second value by replacing it with two new values:

#Example 18

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Example 19

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

# ans ['apple', 'banana', 'watermelon', 'cherry']

# example 20

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# in this code the append function adds the element of orange

# example 21

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# in this code the orange is added to the list after apple

# example 22

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Example 23 

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 

# Example 23

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Example 24

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Example 25

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Example 26

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Example 27

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# Example 28

thislist = ["apple", "banana", "cherry"]
del thislist

# Example 29

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Example 30

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Example 31
  
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# Example 32
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# Example 34
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Example 35

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Example 36

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# Example 37

newlist = [x for x in fruits if x != "apple"]

# Example 38

newlist = [x for x in range(10)]

# Ex 39

newlist = [x for x in range(10) if x < 5]

# Ex 40

newlist = [x.upper() for x in fruits]

# Ex 41

newlist = ['hello' for x in fruits]

# Ex 42

newlist = [x if x != "banana" else "orange" for x in fruits]

#Ex 43

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Ex 44

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


# Ex 45

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Ex 46

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Ex 47

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Ex 48

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Ex 49

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Ex 50

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Ex 51

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Ex 52

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Ex 53

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Ex 54

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Ex 55

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Exercises 

# Task  1


fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Task 2

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Task 3

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Task 4

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")

# Task 5

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Task 6

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Task 7

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Task 8

fruits = ["apple", "banana", "cherry"]
print(len(fruits))



















