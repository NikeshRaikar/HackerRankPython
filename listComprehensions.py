x = input()
y = input()
z = input()
n = input()

list1 = []
for i in range (x+1):
    list1.append(i)
list2 = []
for j in range(y+1):
    list2.append(j)
list3 = []
for k in range(z+1):
    list3.append(k)


# list comprehension code here
list4 = [[i, j, k] for i in list1
                   for j in list2
                   for k in list3 if (i+j+k) != n]

print (list4)
