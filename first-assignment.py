#!/usr/bin/env python
# coding: utf-8

# In[3]:


poem = """Twinkle, twinkle, little star,
                How I wonder what you are!
                        Up above the world so high,
                        Like a diamond in the sky.

          Twinkle, twinkle, little star,
                How I wonder what you are"""
print(poem)


# In[27]:


import platform
print('Python current version')
print(platform.python_version())


# In[28]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[18]:


print('Please enter the value of circle radius')
radius = int(input())
area = 3.14 * (radius ** 2 )
print('Area')
print(area)


# In[25]:


print('Please enter first name')
firstName = input()
print('Please enter last name')
lastName = input()
print('Reversed full name')
print(lastName + ' ' + firstName)


# In[23]:


print('Please enter value-1 for addition')
value1 = int(input())
print('Please enter any value-2 for addition')
value2 = int(input())
print('Total') 
print(value1 + value2)


# In[ ]:




