#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2nd max element in the list by traversing just once through the list
l1=[5,6,7,8,-2,4,9,-1,3]
if l1[0]>l1[1]:
    max1=l1[0]
    max2=l1[1]
else:
    max2=l1[0]
    max1=l1[1]
for i in l1[2:]:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2:
        max2=i
        
print(max2)

#method2 - 2min & 2nd max element in the list
list1=[5,6,7,8,-2,4,9,-1,3]
list1.sort()
print(list1)
min2=list1[1]
max2=list1[-2]
print("2nd Min: ",min2," & 2nd Max: ",max2)

#method3 - 2nd min element in the list
lst1=[5,6,7,8,-2,4,9,-1,3]
lst1.remove(min(lst1))
print(min(lst1))


#min element in the list
list1=[5,6,7,8,-2,4,9,-1,3]
mini=list1[0]
for i in list1:
    if i<mini:
        mini=i
print(mini)

#method 2 - min element in the list
list1=[5,6,7,8,2,4,9,1,0,3]
for i in range(len(list1)):
    for j in range(len(list1)):
        if list1[j]<list1[i]:
            mini=list1[j]
        else: #not necessarily required
            continue
print(mini)

