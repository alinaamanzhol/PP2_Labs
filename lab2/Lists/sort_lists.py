thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)  #Sort the list descending
print(thislist)


thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)   #Sort the list based on how close the number is to 50
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()  #Case sensitive sorting can give an unexpected result
print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)  #Perform a case-insensitive sort of the list
print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() 
print(thislist)