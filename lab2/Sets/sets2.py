thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
  
  
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)  #Union joins items from both sets, exclude duplicates
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3} 
set3 = set1 | set2  # | means union
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)


x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)  #joining a set with tuple
print(z)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)  #method inserts the items in set2 into set1, exclude duplicates
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)  #keeps only duplicates
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2  # & means intersection
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)  #changes the original set
print(set1)



set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)  #Keep all items from set1 that are not in set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2  # - means difference too
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)  #keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)  #Keep the items that are not present in both sets
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2  # ^ is symmetric difference
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)  #method to keep the items that are not present in both sets
print(set1)