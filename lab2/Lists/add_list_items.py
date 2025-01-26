thislist = ["apple", "banana", "cherry"]
thislist.append("orange") #add to the end of a list
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") #To insert a list item at a specified index
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) #To append elements from another list to the current list
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) #Add elements of a tuple to a list
print(thislist)