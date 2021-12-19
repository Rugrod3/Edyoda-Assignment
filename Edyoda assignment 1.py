#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=0
y=1
while y<50:
    print(y)
    x,y=y,x+y


# In[3]:


word=input()
for char in range(len(word)-1,-1,-1):
    print(word[char],end="")


# In[6]:


no_list=[1,2,3,4,5,6,7,8,9,10]
count_even=0
count_odd=0
for i in no_list:
    if i%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print('no.of even number:',count_even)
print('no, of odd number:',count_odd)


# In[ ]:




