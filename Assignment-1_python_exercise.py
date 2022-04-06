#!/usr/bin/env python
# coding: utf-8

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ** What is 7 to the power of 4?**

# In[2]:


a=7
b=4
print(a^b)


# ** Split this string:**
# 
#     s = "Hi there Sam!"
#     
# **into a list. **

# In[3]:


s="Hi there Sam!"
print(s.split())


# In[4]:


print(s.split())


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[5]:


planet = "Earth"
diameter=12742
print(f"The diameter of {planet} is {diameter} kilometers.")


# In[ ]:





# ** Given this nested list, use indexing to grab the word "hello" **

# In[7]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[8]:


lst[3][1][2]


# ** Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

# In[10]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[ ]:





# ** What is the main difference between a tuple and a list? **

# tuple is immutable and list is mutaable

# ** Create a function that grabs the email website domain from a string in the form: **
# 
#     user@domain.com
#     
# **So for example, passing "user@domain.com" would return: domain.com**

# In[14]:


str="user@domain.com"
a=str.split("@")
a[1]


# In[15]:


print(a[1])


# ** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

# In[21]:


a="dog has a tail"
if 'dog' in a.lower():
        print("True")


# In[24]:


a="snoppy is a dog and dog has a tail"
count = 0
for word in a.lower().split():
    if word == 'dog' or word == 'dogs':
        count = count + 1
print(count)


# ** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

# In[ ]:





# In[ ]:





# ### Final Problem
# **You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big    Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all 
#   cases. **

# In[16]:


def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speeding = speed - 5
    else:
        speeding = speed
    
    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'


# In[17]:


caught_speeding(69,"True")


# In[20]:


caught_speeding(89,"True")


# # Great job!
