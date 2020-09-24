#!/usr/bin/env python
# coding: utf-8

# In[1]:


correct_item = input('Please input an object. Lowercase please. \n')
userlist = ('apple', 'banana', 'corn', 'dessert')

while True:
    if correct_item in userlist:
        print('Yay! You got it right!')
        break
    else:        
        correct_item = input('Please input an object. Lowercase please. \n');


# In[1]:


def checknumber(usernumbers):
    for numbers in usernumbers:
        if numbers.isdigit():
            return True 
        else:
            return False 
        
userinput = input('Please input your numbers separated by commas: \n')
userinput = userinput.split(',')

while True:
    if checknumber(userinput) == True:
        newlist_numbers = [int(i) for i in userinput]
        sumnumbers = sum(newlist_numbers)
        print(sumnumbers)
        break
    else:
        userinput = input('Please input your numbers separated by commas: \n')
        userinput = userinput.split(',');

