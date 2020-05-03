
# coding: utf-8

# In[22]:


import numpy as np
def arr_replace(array1):
    array1[array1%2! = 0] = 0
    return array1
print (arr_replace(np.array([1,2,3,4,5,6,7,8,9])))        


# In[30]:


import numpy as np
def arr_replace_where (array1):
    array1 = np.array([1,2,3,4,5,6,7,8,9]) 
    result = np.where(array1%2==0, 0, array1)
    return array1, result
print(arr_replace_where (np.array([1,2,3,4,5,6,7,8,9])))


# In[38]:


import numpy as np
def arr_repeat (array1):
    x = np.repeat(array1, 2)
    return x
print (arr_repeat(np.array([1,2,3,4,5,6,7,8,9])))


# In[37]:


import numpy as np
def arr_join (array1):
    x = np.tile(array1, 2)
    return x
print (arr_join(np.array([1,2,3,4,5,6,7,8,9])))


# In[40]:


import numpy as np
def arr_intersection (array1, array2):
    return np.intersect1d (array1, array2)
print (arr_intersection([1, 3, 4, 3], [3, 1, 2, 1]))


# In[72]:


import numpy as np
print (np.random.uniform(5.0, 10.0, 2))

