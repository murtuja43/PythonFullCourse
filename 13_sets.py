numbers = {1, 3, 4, 5, 6, 8}
print(numbers)


fruits = {"Apple", "Banana", "Cherry", "Apple"}
print(fruits, type(fruits))

fruits.add("Grape") #add new item
print(fruits)

fruits.remove("Cherry") #remove an item
print(fruits)


fruits1 = {"Apple", "Banana", "Cherry", "Mango"}
fruits2 = {"Grape", "Orange", "Mango", "Apple"}

all_fruits = fruits1.union(fruits2)
print(all_fruits)

common_fruits = fruits1.intersection(fruits2)
print(common_fruits)


a = {}
print(type(a))


b = set()  #empty set
print(type(b))