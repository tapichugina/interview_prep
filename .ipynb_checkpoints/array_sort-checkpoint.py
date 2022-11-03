#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
import sys


# In[24]:


# test cases
test=[0,0,10,2]


# In[27]:


# space complexity O(n^2)

def insertion_sort(arr):
    print(arr)
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
                arr[j+1]=arr[j]
                j-=1
        arr[j+1]=key       
    print(arr)
    return arr


# In[28]:


insertion_sort(test)


# In[ ]:




