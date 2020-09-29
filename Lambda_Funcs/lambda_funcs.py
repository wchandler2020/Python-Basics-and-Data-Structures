# add5 = lambda x: x + 5
# print(add5(7))


list1 = [('eggs', 2.25), ('honey', 5.70), ('carrots', 2.50), ('peaches', 3.50)]

list1.sort(key= lambda x : x[1])
print(list1)
