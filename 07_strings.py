name = "Trump"

name1 = name[3]
print(name1)

name2 = name[0:3] #start from 0, all the way till 3, excluding 3
name3 = name[-5:-2] #these 2 lines are same

print(name2, name3)

name4 = name[:5] #same as [0:5]
name5 = name[0:] #same as [0:5]
name6 = name[1:] #same as [1:5]
print(name4, name5, name6)


word = "extraordinary"

word2 = word[1:9:3] #this is called skip value
print(word2)
