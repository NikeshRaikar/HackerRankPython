x = input()
list1 = []
for i in range (x):
    list1.append(i)
list1.append(x)


y = input()
list2 = []
for j in range(y):
    list2.append(j)
list2.append(y)


z = input()
list3 = []
for k in range(z):
    list3.append(k)
list3.append(z)

n = input()
# print (list1)
# print (list2)
# print (list3)

# list comprehension code here

# l1=[x*x for x in [0, 1, 2, 3] if (x%2==0)]
list4 = [[i, j, k] for i in list1
                   for j in list2
                   for k in list3 if (i+j+k) != n]

print (list4)


#Parameters
#The list comprehension basically consists of four parameters.
#    newlist = [output_expression(x) for x in oldlist if conditional(x)]
#Output expression: Defines the output of the list
#Oldlist: Defines the list which is to be traversed
#Conditional/predicate: Defines a condition on variable x. This is an optional parameter.
#Newlist: Save the result of list expression in the newlist