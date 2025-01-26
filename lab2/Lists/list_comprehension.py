thislist = ["apple", "banana", "cherry"]
for x in thislist:  #Print all items in the list, one by one
  print(x)
  
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):  #Print all items by referring to their index number
  print(thislist[i])
  
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"] #Only accept items that are not "apple"
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)


newlist = [x for x in range(10)]
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


newlist = [x for x in range(10) if x < 5]
print(newlist) #[0, 1, 2, 3, 4]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits] #all words in uppercase
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits] #['hello', 'hello', 'hello', 'hello', 'hello']
print(newlist)



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits] #['apple', 'orange', 'cherry', 'kiwi', 'mango']
print(newlist)


