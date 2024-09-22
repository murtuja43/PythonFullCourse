# So, what is a tuple in Python?

# A tuple is a collection of items, just like a list. But here’s the difference: tuples cannot be changed after you create them. Once you put items in a tuple, you cannot add, remove, or change them.


days_of_week = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(days_of_week)

fruits = ("Mango", "Orange", "Apple", "Banana")
print(fruits)

print(fruits[1])
print(fruits[1:4])


# fruits.append("Grape")
# print(fruits) #invalid because tuples are immutable.


#Overview
# A tuple is a collection of items, just like a list, but it cannot be changed.
# Tuples are created using round brackets.
# You can access tuple items using their index.
# Tuples are great when you want to store things that won’t change, like days of the week.