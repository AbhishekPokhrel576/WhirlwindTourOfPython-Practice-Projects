#!/usr/bin/env python
# coding: utf-8

# ## This is Assignment 06- Abhishek Pokhrel

# ## Requirement 4

# In[51]:


# create a list named list_1

list_1 = [1, 5, 9, 13, 15, 17, 18, 25, 33, 39, 45, 49, 50, 55, 68, 79, 88, 90, 93, 95]

# length of list
print(len(list_1))

# append 3 to list_1
list_1.append(21)
list_1.append(30)
list_1.append(40)
print(list_1)

# use addition operation to append 7 numbers to list_1
list_1 = list_1 + [23, 28, 35, 37, 60, 70, 99]
print(list_1)

# sort list_1
list_1.sort()
print(list_1)


# ## Requirement 5

# In[50]:


list_1 = [1, 5, 9, 13, 15, 17, 18, 21, 23, 25, 28, 30, 33, 35, 37, 39, 40, 45, 49, 50, 55, 60, 68, 70, 79, 88, 90, 93, 95, 99]

# 4th element from list_1
print(list_1[3])

# 15th element from list_1
print(list_1[14])

# 3rd element from the end of list_1
print(list_1[-3])

# 7th element from the end of list_1
print(list_1[-7])

# first four elements from list_1
print(list_1[0:4]) 

# last five elements from list_1
print(list_1[25:31])

# Elements in reverse order
print(list_1[::-1])

# set the 14th element to -99
list_1[14] = -99
print(list_1)

# every other element in the list
print(list_1[::2])

# set elements 9th through 15th to -77
list_1[9:16] = [-77, -77, -77, -77, -77, -77, -77]
print(list_1)


# ## Requirement 6

# In[49]:


tuple_1 = (1, 12, 13, 19, 21, 27, 28)

# Note: you cannot change the size or content for tuples. They are immutable therefore you can't use tuple_1[3] = -33
# you cannot use tuple_1.append(-22) either since you can't add or assignment anything to a tuple. Once tuple is created
# their size and content cannot be changed. It will give you error. I attempted it and took it out since it gave error as
# mentioned in chapter 06. I got the same error

print(tuple_1)


# ## Requirement 7

# In[48]:


# populate the dictionary with player positions as keys, and player name as value
players_basketball = {'PG': 'LebronJ', 'SG': 'KlayT', 'SF': 'KevinD', 'PF': 'AnthonyD', 'C': 'JoelE', '6thMan': 'DamianL', 'BenchSG': 'BradleyB', 'BenchSF': 'KwahiL', 'BenchPF': 'KristapsP'}

# change a Key::Value Pair
players_basketball['PG'] = 'DamianL'
players_basketball['6thMan'] = 'LebronJ'
print(players_basketball)

# add a new Key::Value Pair

players_basketball['BenchC'] = 'NikolaJ'
print(players_basketball)


# ## Requirement 8

# In[47]:


# Create two sets hatfields and mccoys

hatfields = {'John', 'Lucas', 'Bradley', 'Jacob', 'Ralph', 'AB', 'CJ', 'Adam', 'Amit', 'Ankit'}
mccoys = {'Russell', 'Matt', 'Lucas', 'AB', 'Ankit', 'Moby', 'Bipul', 'Shishir', 'CJ', 'Jamie'}

# union demonstration (two ways: Operator and method)
print(hatfields | mccoys)
print(hatfields.union(mccoys))

# intersection demonstration (two ways: Operator and method)
print(hatfields & mccoys)
print(hatfields.intersection(mccoys))

# difference demonstration (two ways: Operator and method)
print(hatfields - mccoys)
print(hatfields.difference(mccoys))

#symmetric difference (two ways: Operator and method)
print(hatfields ^ mccoys)
print(hatfields.symmetric_difference(mccoys))


# ## Requirement 9

# In[46]:


# Demonstrate the use of if, elif, and else statements based on weather conditions
# temeprature is described as 65 degree Farenheit

temperature = 65

if temperature == 40:
    print('Wear atleast 3 layers and a long Coat')
elif temperature == range(41, 60):
    print('Wear atleast 3 layers')
else:
    print('Wear a long sleeve shirt')


# ## Requirement 10

# In[44]:


# Demonstrate the use of a for loop using Range
for x in range(20):
    print(x, end='  ')


# In[45]:


# Demonstrate the use of a for loop using list contents
for i in list(range(0, 30, 2)):
    print(i, end='  ')


# ## Requirement 11

# In[175]:


# Demonstrate the use of the below in two while loops i = 0 to 7

i = 0
while i < 7:
    print(i, end='  ')
    i += 1


# In[177]:


# Demonstrate the use of the blew in two while loops i = 1 to 7
x = 1
while x <= 7:
    print(x, end='  ')
    x += 1


# ## Requirement 12

# In[41]:


# Define and use a function named factorial()
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

print(factorial(7))


# ## Requirement 13

# In[202]:


# Define and use a function named vegetables() args as number of vegetable, kwargs as name of vegetable

def Vegetables(*args, **kwargs):
    print("args =", args)
    print("kwargs = ", kwargs)
    
Vegetables(3, 5, 7, zuchini=3, potatoes=5, cauliflower=7)


# ## Requirement 14

# In[43]:


# create a list named cars that contains three dictionaries each with three key::value pairs
# three dictionaries with three key::value pairs
Cars = [{'power steering': '100', 'sun roof': '300', 'side camera': '500'},
        {'power steering': '200', 'sun roof': '250', 'side camera': '275'},
        {'power steering': '150', 'sun roof': '350', 'side camera': '550'}]

# sort pricewise by power steering from least to greatest $$ using lamda
print(sorted(Cars, key=lambda item: item['power steering']))

# sort pricewise by side camera from least to greatest $$ using lamda
print(sorted(Cars, key=lambda item: item['side camera']))


# ## Requirement 15

# In[53]:


# Demonstrate the use of a try and except statement

try:
    num = int(132)
    assert num % 2 == 0
    print("Its an Even Number!")
except:
    print("Not an even number!")


# ## Requirement 16

# In[59]:


# Demonstrate the use of try, except, else, and finally statements

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
else:
    if age < 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')
finally:        
        print('Hilltop Bar Management')


# ## Requirement 17

# In[ ]:


# Iterator indirection helps us create a vast range, but the program will not instanciate everything at once. 
# Depending upon how much we want to use in the program, we can utilize iterator indirection to run it against our code.
# This allows us to use the benefit of the program without fully creating a list notably.


# ## Requirement 18

# In[60]:


# Create a list of 10 animal species named animals_list and demonstrate the 
# use of len() and iteration to print the index and values

animals_list = ['Leopard', 'Rhino', 'Elephant', 'Tiger', 'Lion', 'Girraffe', 'Wolf', 'Eagle', 'Fox', 'Hippo']
for index in range(len(animals_list)):
    print(index, animals_list[index])


# ## Requirement 19

# In[61]:


# Use the enumerate iterator to perform the same actions as the previous requirement.
for index, val in enumerate(animals_list):
    print(index, val)


# ## Requirement 20

# In[63]:


# Create a list of 10 colors named colors_list. Use the zip iterator
#  print the values of the animals_list and colors_list within the same for loop.

colors_list = ['Blue', 'Black', 'Green', 'Orange', 'Yellow', 'Pink', 'Red', 'Purple', 'Turquoise', 'Grey']

for cval, aval in zip(colors_list, animals_list):
    print(cval, aval)


# ## Requirement 21

# In[64]:


# Create a lambda named times_ten that multiplies the variable x by 10. 
# Use the map iterator and range(10) to evaluate the lambda in a for loop.

times_ten = lambda x: x * 10
for val in map(times_ten, range(10)):
    print(val, end='  ')


# ## Requirement 22

# In[65]:


# Create a lambda named by_three that returns true if the variable x is evenly divisible by 3. 
# Use the filter iterator and range(30) to evaluate the lambda in a for loop.

by_three = lambda x: x % 3 == 0
for val in filter(by_three, range(30)):
    print(val, end='  ')


# ## Requirement 23

# ## This assignment was definitely not easy. It was very very challenging. I enjoyed trying to figure it out and working through the examples and concepts provided on the book, but I also must admit that learning Python would be much much easier if there was someone teaching me personally in my opinion, in class room setting with proper instructions. I'm saying this because i'm more of a person that learns better in that type of setting with an instructor, and it also doesn't help that the this book has some misconceptions on these chapters specially the chapter regarding where it explains dictionaries, it uses the wrong syntax, which I had to figure out on my own. Overall, even though it was extremely hard and time consuming for me, I enojoyed it and told myself that this is a completely new language for me and it will take time to master it.
