thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #deleting the element of a list(removing)
print(thislist)


thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") #remove the first occurence of "banana"
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #removing the second item of a list
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop() #if the index is not mentioned, it removes the last item
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0] #del removes the specified index too
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist #deleting the whole list


thislist = ["apple", "banana", "cherry"]
thislist.clear() #empties the list, the list still remains but it has no content
print(thislist)