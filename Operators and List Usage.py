#!/usr/bin/env python
# coding: utf-8

# # This is Assignment 05 - Abhishek Pokhrel

# ## Requirement 4

# In[183]:


# Demonstrate Arithmetic Operations

# Addition
x = 9 + 12
print(x, "= 9 + 12")

# Substraction
x = 7 - 5
print(x, "= 7 - 5")

# Multiplication
x = 5 * 6
print(x, "= 5 * 6")

# True Division
x = 36 / 6
print(x, "= 36 / 6")

# Floor Division
x = 38 // 6
print(x, "= 38 // 6")

# Exponentiation
x = 2 ** 5
print(x, "= 2 ** 5")


# ## Requirement 5

# In[184]:


# Demonstrate Comparison Operations

# a equal to b
a = [5, 7, 9]
b = [5, 7, 9]
a == b
print(bool(a == b))

# a not equal to b
a = [8, 9, 15]
b = [7, 15, 14]
a != b
print(bool(a != b))

# a less than b
a = 15
b = 20
a < b
print(bool(a < b))

# a greater than b
a = 15
b = 10
a > b
print(bool(a > b))

# a less than or equal to b
a = 4 
b = 5
a <= b
print(bool(a <= b))

# a greater than or equal to b
a = 5
b = 10
a >= b
print(bool(a >= b))


# ## Requirement 6

# In[121]:


get_ipython().system('python operators.py')


# ## Requirement 7

# In[130]:


# define list_1 and list_2
list_1 = [2, 4, 12, 15, 18, 20, 25, 31, 33, 40]
list_2 = [3, 5, 7, 10, 16, 38, 100, 159, 70, 71]
# define list_even and list_odd
list_even = []
list_odd = []
for i in list_1:
    if (i % 2) == 0:
        list_even.append(i)
    else: 
        list_odd.append(i)
for i in list_2:
    if (i % 2) == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print("list_even =", list_even)
print("list_odd =", list_odd)


# ## Requirement 8

# In[140]:


x = 1.3
print(x.is_integer())


# ## Requirement 9

# In[166]:


# demonstrate Boolean, Identity, and membership operations

# and
x = 9
print(bool((x > 4) and (x < 11)))

# or
x = 11
print(bool((x > 10) or (x % 2 == 0)))

# not
x = 51
print(bool(not(x < 54)))

# is
a = [ 5, 6, 8]
b = [5, 6, 8]
print(bool(a is b))

# is not
c = [5, 6, 8]
d = [5, 6, 8]
c = d
print(bool(c is not d))

# in
f = [1, 5, 7, 9]
print(bool(9 in f))

# not in
g = [6, 8, 10, 12]
print(bool(10 not in g))

# object identity
# The identity operators, "is" and "is not" check for object identity
m = [2, 3, 4]
n = [2, 3, 4]
m = n
print(bool(m is n))
print(bool(m is not n))


# ## Requirement 10

# In[172]:


# demonstrate variable precision using ceil(), trunc()
# and floor()
 
# importing "math" for precision function
import math
 
# initializing value
x = 65.7685439821

# use trunc() to print integer after truncating
print("The integral value of number is : ", end="")
print(math.trunc(x))
 
# use ceil() to print number after ceiling
print("The smallest integer greater than number is : ", end="")
print(math.ceil(x))
 
# using floor() to print number after flooring
print("The greatest integer smaller than number is : ", end="")
print(math.floor(x))


# ## Requirement 11

# In[182]:


# demonstrate String operations

message = "what is your name?"
response = "abhishek pokhrel"

# length of string
print(len(response))

# Make upper case
print(response.upper())

# Capitalize
print(message.capitalize())

# concatenation
print(message + response)

# multi-concatenation
print(3 * response)

# access of individual characters
print(response[7])


# # My experience with assignment 5 I'd say would be fairly good. This is because I am completely new to python or any computer language for that matter since I did my bachelor's in biology and i'm trying to learn python in order to make it easier for me when I start my masters in Financial Technology and data analytics next year. I say that it was fairly good because requirements 4,5,6,7,8,9, and 11 were failry straight forward with practice I was able to get them, but requirement 10 wasn't taught at all in any of the chapters from 00-05 and was completely out of context for this assignment; nevertheless, I was able to research and learn about what variable precision is and what trunc(), ceil() and floor() functions meant. 
