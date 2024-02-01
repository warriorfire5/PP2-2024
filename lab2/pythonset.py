#Example 1
myset = {"apple", "banana", "cherry"}

#Example 2

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Example 3

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#Ans {True, 2, 'banana', 'cherry', 'apple'}

#Example 4

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#Example 5

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Example 6

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Example 7

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#Example 8

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#Example 9

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Example 10

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Example 11

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#Example 12

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#Example 13

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Example 14

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#Exercises 
#Task 1

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#Task 2
  
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Task 3

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#Task 4

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#Task 5

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")








