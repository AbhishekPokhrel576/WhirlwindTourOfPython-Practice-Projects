#!/usr/bin/env python
# coding: utf-8

# ## This is Assignment 07- Abhishek Pokhrel

# ## Requirement 4

# In[14]:


# use list comprehension to output a list with numbers that are not multiples of 3 and not equal to 13 and not equal to 17

L = [i for i in range(1, 30) if i % 3 > 0]
remove_list = [13 , 17]
M = [i for i in L if i not in remove_list]
print(M)


# ## Requirement 5

# In[15]:


# previous Requirement but using loop syntax instead of list comprehension

L = []
for val in range(1, 30):
    if val % 3 > 0:
        L.append(val)
L.remove(13)
L.remove(17)
print(L)


# ## Requirement 6

# In[16]:


#  range(30), use list comprehension to output a list with positive numbers that are even and negative numbers that are odd

L = [val if val % 2 == 0 else -val
    for val in range(0, 30)]
print(L)


# ## Requirement 7

# In[17]:


# range(1000), use set comprehension to output a set of numbers based on i % 5

L = {i for i in range(1, 1000) if i % 5 == 0}
print(L)


# ## Requirement 8

# In[18]:


# From range(20), use dictionary comprehension to output a dictionary of numbers 
# (i) as keys and their cubes (i**3) as values

L = {i:i**3 for i in range(20)}
print(L)


# ## Requirement 9

# In[1]:


# From range(50), use a generator function to create a generator named G of even numbers, 
# print the type of G, and then print the contents of G

G = (i*2 for i in range(50))
print(G)

G = (i*2 for i in range(50))
print(list(G))
print(type(G))  # for extra to show that its a generator

# or you can print the contents of G by making it into a list like this as well

G = [i*2 for i in range(50)]
print(G)


# ## Requirement 10

# In[8]:


# From range(15), use a generator in two ways to output n/2
# as G1 = (…) 

G1 = [i/2 for i in range(15)]
print(G1)

# as G2 = gen_divby2().

def gen_divby2():
    for i in range(15):
        yield i / 2

G2 = gen_divby2()
print([*G2])


# ## Requirement 11

# In[9]:


# Use a generator defined as a function to output prime numbers < 100

def gen_primes(N):
    """Generate primes leading up to N"""
    primes = set()
    for n in range(2, N):
        if all(n % p > 0 for p in primes):
            primes.add(n)
            yield n

print(*gen_primes(100))


# ## Requirement 12

# In[10]:


# Import the following modules from Python’s Standard Library.
# Demonstrate a minor example using functionality/capability from each module in the list

## os and sys

import os
f = os.listdir("D:\WPy64-3950")
print(f)
# Above example I have used os library to list the directory mentioned above.
import sys
print(sys.version)
# above example I have used system library module to list the Python interpreter version

## math and cmath

import math
L = math.ceil(11.27981)
print(L)

import cmath
G = cmath.sqrt(complex(81.0, 144.0))
print(G)

## itertools

from itertools import permutations
l = permutations(range(5))
print(*l)

## functools

from functools import reduce

M = [10, 15, 20 ,25]
list_product = reduce(lambda x,y: x*y, M)
print(list_product)

## random

import random
print(random.randint(0, 100))

## pickel

import pickle

d = []
for i in range(3):
    r = input('Enter d '+str(i)+' : ')
    d.append(r)

file = open('important', 'wb')

pickle.dump(d, file)
file.close()

## json and csv

import json

x = '{"name": "Abhishek", "age": "25", "city": "Austin"}'
y =  json.loads(x)
print(y["age"])

import csv
fields = ['Name', 'Position', 'DOB']
rows = [['Abhi', 'PG', '2001'],
        ['Arun', 'SG', '1999'],
        ['Amit', 'SF', '1998'],
        ['Shshir', 'PF', '1999'],
        ['Bipul', 'C', '2001']]
filename = "Highschool_Basketball.csv"

with open(filename, 'w') as csvfile:
    
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows((rows))


# In[11]:


# urllib

import urllib.request
request_url = urllib.request.urlopen('https://www.google.com/')
print(request_url.read())


# ## Requirement 13

# In[12]:


# Demonstrate the conversion to upper-case and lower-case

Phrase = "THis GuY is extremely ANNOYinG."
print(Phrase.upper())
print(Phrase.lower())

# Convert “this is the title of my latest novel” to a title

Phrase = "this is the title of my latest novel."
print(Phrase.title())

# Removing leading and trailing spaces

Sentence = '    THis GuY is extremely ANNOYinG.   '
print(Sentence.rstrip())  # Removing space to the right
print(Sentence.lstrip())  # Removing space to the left
print(Sentence.strip())   # Removing all white spaces leading and trailing spaces

# Remove leading zeros

Number = "00045679890000"
print(Number.strip('0'))

# Return the index of a substring

Phrase = "This very fast guy ran a mile in five minutes and four seconds"
print(Phrase.index('fast'))

# Determine if a string ends with and begins with a substring

Phrase = "This very fast guy ran a mile in five minutes and four seconds"
print(Phrase.endswith('five'))
print(Phrase.startswith('This'))
print(Phrase.endswith('seconds'))

# Replace a substring with another substring

Phrase = "This very fast guy ran a mile in five minutes and four seconds"
print(Phrase.replace('fast', 'slow'))

# Split a string of words into a list of individual words

Phrase = "This very fast guy ran a mile in five minutes and four seconds"
print(Phrase.split())

# Join a list into a string using ** as separators

list = ['my', 'sugar', 'bomb']
joined = " ".join(list)
separator = "**"
joined = separator.join(list)
print(joined)

# Print list elements each on its own line using join()

list1 = ['my', 'sugar', 'bomb']
print('\n'.join(list1))

# Define pi = ‘3.14159265359’ Use format() to print pi to 7 decimal places to the right of the decimal point.

pi = 3.14159265359
print("pi = {0:.7f}".format(pi))


# ## Requirement 14

# In[13]:


# Use the Regular Expression compile() method to create an email matcher
# and demonstrate the matcher with 3 valid emails and 3 invalid emails

import re
email_regex = re.compile(r'(?P<user>[\w.]+)@(?P<domain>\w+)\.(?P<suffix>[a-z]{3})')

email1 = "abhi.lxgnd@gmail.com"
email2 ="abhi_23dharma@yahoo.com"
email3 ="amitk@gmail.com"
email4 ="randi237@hotmail."
email5 ="rondo.obama@skycm"
email6 ="romeo.kc57576@yahoocom"

print(email_regex.match(email1) != None)
print(email_regex.match(email2) != None)
print(email_regex.match(email3) != None)
print(email_regex.match(email4) != None)
print(email_regex.match(email5) != None)
print(email_regex.match(email6) != None)


# ## Requirement 15

# ## My Experience with this assignment was just the same as the last one. It was most definitely very very challenging and I did the most amount of research outside of studying the chapters for this assignment more than any other assignment. Specially the last requirement for valid and invalid email was very very hard and took me a very long time to figure out. I did have to also do a lot more trial and errors for other requirements as well. I am very excited about using everything I learnt from this book and go into the other book.
