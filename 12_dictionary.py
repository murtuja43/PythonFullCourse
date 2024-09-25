# A dictionary in Python is a collection of key-value pairs. Each item in a dictionary has a key and a value.

a = {
    "Elon" : 23,
    "Bruce" : 24,
    "Charles" : 21,
    "Logan" : 20
}

print(a, type(a))
print(a.keys())
print(a.values())
print(a["Logan"])

a.update({"Logan" : 24, "Janet" : 18})
print(a) #the main dictionary will change (because dict is mutable)