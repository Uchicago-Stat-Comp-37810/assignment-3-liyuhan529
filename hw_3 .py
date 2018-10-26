# Name: Yuhan Li
# hw3.py

import math
import random
##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here

##### YOUR CODE HERE #####
def is_divisible(m,n):
    if n==0:
        return("denominator couldn't be zero")
    else:
        return(m%n==0)

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print (is_divisible(10, 5)) # This should return True
print (is_divisible(18, 7))  # This should return False
print (is_divisible(42, 0))  # What should this return?

# ********** Exercise 2 ********** 

# Define not_equal function here
##### YOUR CODE HERE #####
def not_equal(m,n):
    if m==n:
        return False
    else:
        return True
    
# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal(5,6))
print(not_equal(4,4))
print(not_equal("a","b"))
print(not_equal("a","a"))
print(not_equal([1,3,5],[1,2,3]))
print(not_equal([1,2,3],[1,2,3]))
print(not_equal("a",3))
print(not_equal("4",4))


# ********** Exercise 3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####
def multadd(a,b,c):
    return(a*b+c)


## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
angle_test=multadd(math.cos(math.pi/4),0.5,math.sin(math.pi/4))
print ("sin(pi/4) + cos(pi/4)/2 is:")
print (angle_test)

ceiling_test = multadd(math.log(12,7),2,math.ceil(276/19))
print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####
def rand_divis_3():
    x=random.randint(0,100)
    print("the random number we generate is",x)
    if x%3==0:
        return True
    else:
        return False

# Test Cases
##### YOUR CODE HERE #####
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())

