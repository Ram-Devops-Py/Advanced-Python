#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Built in functions 

import numpy as np
array_of_zeros = np.zeros((3,4))
array_of_zeros


# In[19]:


print(array_of_zeros)


# In[21]:


array_of_ones = np.ones((3,4))
array_of_ones


# In[27]:


array_of_ones_int = np.ones((2,3),dtype = np.int16)
array_of_ones_int


# In[26]:


#Empty array
array_empty = np.empty((2,3))
array_empty


# In[37]:


#Identity matrix 
array_eye = np.eye((5),dtype = np.int32)
array_eye


# In[39]:


# Even numbers from 1-21

array_of_evens = np.arange(2,21,2)
print(array_of_evens)


# In[ ]:




