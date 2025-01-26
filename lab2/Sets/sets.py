myset = {"apple", "banana", "cherry"}  #Set items are unordered, unchangeable, and do not allow duplicate values.


thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  #banana, cherry, apple


thisset = {"apple", "banana", "cherry", True, 1, 2}  #True and 1 is considered the same value:  
print(thisset)


thisset = {"apple", "banana", "cherry", False, True, 0}  #0 and False is considered the same value
print(thisset)


thisset = {"apple", "banana", "cherry"}
print(len(thisset))  #3


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"} #a set can contain different data types


myset = {"apple", "banana", "cherry"}
print(type(myset))  #class <set>


thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members. Can remove and add new items
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.


thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
  
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  #"True"


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)  #False


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")  #removing the element
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()  #removing random item
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()  #emptying the set
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset  #deleting the set
print(thisset)