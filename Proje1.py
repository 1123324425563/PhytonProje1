#!/usr/bin/env python
# coding: utf-8

# In[16]:


m = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


# In[18]:


print (m)
        


# In[21]:


for l in m:
    print (l)


# In[37]:


new_m= []
for l in m:   
    for e in l:
        new_m.append(e)
          for l in m:


# In[38]:


print(new_m)


# In[68]:


a=['cat']


# In[75]:


for l in a:
    print (l)


# In[81]:


b=[3]
for l in b:
    print(l)


# In[82]:


c=[1, 'a','dog']


# In[83]:


x=a+b+c


# In[85]:


print(x)


# In[86]:


l2=[[1, 2], [3, 4], [5, 6, 7]]


# In[114]:


for i in reversed (l2):
    print(i)


# In[ ]:




