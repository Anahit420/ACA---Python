
# coding: utf-8

# In[2]:


def implications3(a,b,c):
    return a and b and not 
print (implications3(1,0,0))


# In[3]:


#Is polindrome or not
def canFormPalindrome(str):
    list = []
    for i in range(len(str)):
        if str[i] in list:
            list.remove(str[i])
        else:
            list.append(str[i])
    if (len(str) % 2 == 0 and len(list) == 0 or            (len(str) % 2 == 1 and len(list) == 1)):
        return True
    else:
        return False
if (canFormPalindrome("abbab")):
    print("True")
else:
    print("False")

