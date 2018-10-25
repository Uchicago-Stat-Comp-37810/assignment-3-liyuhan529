#!/usr/bin/env python
# coding: utf-8

# # Stat 378 HW3
# 
# By Yuhan Li

# In[35]:


import math
import random
# Ex1
# define the function is_divisible
def is_divisible(m,n):
    if n==0:
        return("denominator couldn't be zero")
    else:
        return(m%n==0)


# In[28]:


#test the function is_divisible
print(is_divisible(4,2))
print(is_divisible(4,0))
print(is_divisible(8,3))
print(is_divisible(4,-2))


# In[29]:


#Ex2
#define the function not_equal
def not_equal(m,n):
    if m==n:
        return False
    else:
        return True
        


# In[30]:


# test the function not_equal
print(not_equal(5,6))
print(not_equal(4,4))
print(not_equal("a","b"))
print(not_equal("a","a"))
print(not_equal([1,3,5],[1,2,3]))
print(not_equal([1,2,3],[1,2,3]))
print(not_equal("a",3))
print(not_equal("4",4))


# In[32]:


#Ex3
#1.define the function multadd
def multadd(a,b,c):
    return(a*b+c)
# test the function
print(multadd(1,2,3))


# In[34]:


#2.angle test and ceiling test
print ('sin(pi/4) + cos(pi/4)/2 is:')
print(multadd(math.cos(math.pi/4),0.5,math.sin(math.pi/4)))

print ('ceil(276/19)+2log7(12) is:')
print(multadd(math.log(12,7),2,math.ceil(276/19)))


# In[49]:


#Ex4
#define the function rand_divis_3
def rand_divis_3():
    x=random.randint(0,100)
    if x%3==0:
        return True
    else:
        return False

# test the function
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())


