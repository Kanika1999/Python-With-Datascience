
# coding: utf-8

# In[1]:


# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Plotting functions

def Plotvec1(u, z, v):
   
   ax = plt.axes()
   ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
   plt.text(*(u + 0.1), 'u')
   
   ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
   plt.text(*(v + 0.1), 'v')
   ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
   plt.text(*(z + 0.1), 'z')
   plt.ylim(-2, 2)
   plt.xlim(-2, 2)

def Plotvec2(a,b):
   ax = plt.axes()
   ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
   plt.text(*(a + 0.1), 'a')
   ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
   plt.text(*(b + 0.1), 'b')
   plt.ylim(-2, 2)
   plt.xlim(-2, 2)


# In[3]:


# Create a python list

a = ["0", 1, "two", "3", 4]


# In[4]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# In[6]:


#What is Numpy?
#A numpy array is similar to a list. It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy:

# import numpy library

import numpy as np 


# In[7]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# In[8]:


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])


# In[9]:


# Check the type of the array

type(a)


# In[10]:


# Check the type of the values stored in numpy array

a.dtype


# In[11]:


# Create a numpy array

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])


# In[12]:


# Check the type of array

type(b)


# In[13]:


# Check the value type

b.dtype


# In[14]:


# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c


# In[15]:


# Assign the first element to 100

c[0] = 100
c


# In[16]:


# Assign the 5th element to 0

c[4] = 0
c


# In[17]:


# Slicing the numpy array

d = c[1:4]
d


# In[18]:


# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
c


# In[20]:


#Create the index list

select = [0, 2, 3]


# In[21]:


# Use List to select elements

d = c[select]
d


# In[22]:


# Assign the specified elements to new value

c[select] = 100000
c


# In[23]:


# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
a


# In[24]:


# Get the size of numpy array

a.size


# In[25]:


# Get the number of dimensions of numpy array

a.ndim


# In[26]:


# Get the shape/size of numpy array

a.shape


# In[27]:


# Create a numpy array

a = np.array([1, -1, 1, -1])


# In[28]:


# Get the mean of numpy array

mean = a.mean()
mean


# In[29]:


# Get the standard deviation of numpy array

standard_deviation=a.std()
standard_deviation


# In[30]:


# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
b


# In[31]:


# Get the biggest value in the numpy array

max_b = b.max()
max_b


# In[32]:


# Get the smallest value in the numpy array

min_b = b.min()
min_b


# In[33]:


u = np.array([1, 0])
u


# In[34]:


v = np.array([0, 1])
v


# In[35]:


# Numpy Array Addition

z = u + v
z


# In[36]:


# Plot numpy arrays

Plotvec1(u, z, v)


# In[37]:


# Create a numpy array

y = np.array([1, 2])
y


# In[38]:


# Create a numpy array

u = np.array([1, 2])
u


# In[40]:


# Create a numpy array

v = np.array([3, 2])
v


# In[41]:


#Calculate the production of two numpy arrays

z = u * v
z


# In[42]:


# Calculate the dot product

np.dot(u, v)


# In[43]:


# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u


# In[44]:


# Add the constant to array

u + 1


# In[45]:


#The value of pie

np.pi


# In[46]:


# Create the numpy array in radians

x = np.array([0, np.pi/2 , np.pi])


# In[48]:


#Calculate the sin of each elements

y = np.sin(x)
y


# In[49]:


# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)


# In[50]:


# Makeup a numpy array within [-2, 2] and 9 elements

np.linspace(-2, 2, num=9)


# In[51]:


# Makeup a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)


# In[52]:


# Calculate the sine of x list

y = np.sin(x)


# In[53]:


#Plot the result

plt.plot(x, y)


# In[54]:


u = np.array([1, 0])
v = np.array([0, 1])
z=u-v
z


# In[56]:


# Write your code below and press Shift+Enter to execute

z = np.array([2, 4])
-2*z
z


# In[57]:


a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 0, 1, 0, 1])
a * b


# In[58]:


a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))


# In[59]:


a = np.array([-1, 1])
b = np.array([1, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a,b))


# In[60]:


a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))
print("The dot product is", np.dot(a, b))

