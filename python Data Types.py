
# coding: utf-8

# In[1]:


# Try your first Python output

print('Hello, Python!')


# In[2]:


# Check the Python Version

import sys
print(sys.version)


# In[3]:


# Practice on writing comments

print('Hello, Python!') # This line prints a string
# print('Hi')


# In[4]:


# Print string as error message

frint("Hello, Python!")


# In[6]:


# Try to see build in error message

print("Hello, Python!")


# In[7]:


# Print string and error to see the running order

print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")


# In[8]:


# Write your code below and press Shift+Enter to execute 
print("Hello, world!")


# In[9]:


# Write your code below and press Shift+Enter to execute 
print("Hello, world!") # Print the traditional hello world


# In[10]:


# Integer

11


# In[11]:


# Float

2.14


# In[12]:


# String

"Hello, Python 101!"


# In[13]:


# Type of 12

type(12)


# In[14]:


# Type of 2.14

type(2.14)


# In[15]:


# Type of "Hello, Python 101!"

type("Hello, Python 101!")


# In[16]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(12.0)


# In[17]:


# Print the type of -1

type(-1)


# In[18]:


# Print the type of 4

type(4)


# In[19]:


# Print the type of 0

type(0)


# In[20]:


# Print the type of 1.0

type(1.0) # Notice that 1 is an int, and 1.0 is a float


# In[21]:


# Print the type of 0.5

type(0.5)


# In[22]:


# Print the type of 0.56

type(0.56)


# In[23]:


# System settings about float type

sys.float_info


# In[7]:


#You can change the type of the object in Python; this is called typecasting. For example,
#you can convert an integer into a float (e.g. 2 to 2.0).

#Let's try it:

# Verify that this is an integer

type(2)


# In[8]:


# Convert 2 to a float

float(2)


# In[9]:


# Convert integer 2 to a float and check its type

type(float(2))


# In[10]:


# Casting 1.1 to integer will result in loss of information

int(1.1)


# In[11]:


# Convert a string into an integer

int('1')


# In[12]:


# Convert a string into an integer with error

int('1 or 2 people')


# In[13]:


# Convert the string "1.2" into a float

float('1.2')


# In[14]:


# Value true#boolean data types

True


# In[15]:


# Type of True

type(True)


# In[16]:


# Convert True to int

int(True)


# In[17]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6/2) # float


# In[18]:


# Write your code below. Don't forget to press Shift+Enter to execute the cell
type(6//2) # int, as the double slashes stand for integer division 


# In[19]:


# Addition operation expression

43 + 60 + 16 + 41


# In[20]:


# Subtraction operation expression

50 - 60


# In[21]:


# Multiplication operation expression

5 * 5


# In[22]:


# Division operation expression

25 / 5


# In[23]:


# Integer division operation expression

25 // 6


# In[24]:


# Store value into variable

x = 43 + 60 + 16 + 41


# In[25]:


# Print out the value in variable

x


# In[26]:


# Use another variable to store the result of the operation between variable and value

y = x / 60
y


# In[27]:


# Overwrite variable with new value

x = x / 60
x


# In[28]:


# Name the variables meaningfully

total_min = 43 + 42 + 57 # Total length of albums in minutes
total_min


# In[29]:


# Name the variables meaningfully

total_hours = total_min / 60 # Total length of albums in hours 
total_hours

