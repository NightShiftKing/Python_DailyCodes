list1 = [1,2,3,4,5]

list2 = list1

print(list1, 'list1')

print(list2, 'list2')
list3 = list2

print(list1, 'list1')

print(list2, 'list2')

print(list3, 'list3')

del list1

print(list1, 'list1')

print(list2, 'list2')

print(list3, 'list3')

print(list1)
