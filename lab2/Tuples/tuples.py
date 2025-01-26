thistuple = ("apple", "banana", "cherry")
print(thistuple)


thistuple = ("apple", "banana", "cherry", "apple", "cherry")  #the tuple allows duplicate values
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  #the length of tuple(numbers of items)


thistuple = ("apple",)  #creating a tuple by using a comma
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


tuple1 = ("abc", 34, True, 40, "male") #a tuple can contain different data types


mytuple = ("apple", "banana", "cherry")
print(type(mytuple))  #class "tuple"


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])  #banana


thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])  #cherry


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])  #index from 0, 5 is NOT included and 2 is included



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])   #This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1



thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  
  
