
# coding: utf-8

# import bisect
# def bisect_position (lst):
#     for i in range(len(lst)):
#         bisect.insort(lst,3)
#     return (lst[i])
# print (bisect_position ([1,2,3,6]))

# In[10]:


def all_sums(num):
    lst = []
    num1 = list(range(1,num))
    for i in num1:
        j = num - i
        if j in num1:
            lst.append((i,j))
    return lst
print (all_sums(6))


# In[16]:


from collections import defaultdict
def duplicate_characters(str):
    d = defaultdict(int)
    d1=[]
    for i in str:
        d[i] = d[i]+1
    for i in d:
        if d[i]>1:
            d1.append(i)
    return d1
print (duplicate_characters ('Here we have some duplicate'))


# In[17]:


def compare_lists(l1, l2):
    if set(l1) == set(l2):
        return True
    return False
print (compare_lists([1,1,5,4,2,1,2], [5,1,1,2,4,1,2]))

