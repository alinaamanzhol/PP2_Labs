list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2  #join two lists
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)  #joining two lists
print(list1)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)  #by extending a list1 to add to it the elements of a list2
print(list1)