# In Python, a list is a collection of items. These items can be numbers, words, or even other lists! Lists are very helpful when you need to store multiple things together. Lists are mutable.

shopping_list = ["Bread", "Butter", "Rice", "Milk"]
print(shopping_list)


fruits = ["Mango", "Orange", "Apple", "Banana"]
print(fruits)

print(fruits[1])
print(fruits[1:3])

#methods/functions:

fruits.append("Grape") #this adds a new list item
print(fruits)

fruits.remove("Mango")
print(fruits)

fruits.reverse()
print(fruits)


# --------------------
li = [1, 55, 3, 6, 3]
print(sum(li)) #this sums the list



#Overview
# A list is a collection of items, like numbers or words.
# Lists are created using square brackets, and items are separated by commas.
# You can access items in a list using their index.
# You can add items using append(), and remove them using remove().
# use sum function on list