#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Q 1.

tuple1 =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

List2 =[]
List3 =[]

for t in tuple1:
    List2.append(t[1],)

List2.sort()

for l in List2:
    for q in tuple1:
        if l == int(q[1],):
            List3.append(q)

print(List3)


# In[13]:


#Q.2
my_dict = {}
for i in range(97, 123):
    my_dict[chr(i)] = i
print(my_dict)


# In[ ]:




