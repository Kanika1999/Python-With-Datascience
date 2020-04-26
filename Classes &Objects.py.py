
# coding: utf-8

# In[1]:


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  


# In[2]:


#Create an object RedCircle

RedCircle = Circle(10, 'red')


# In[3]:


# Find out the methods can be used on the object RedCircle

dir(RedCircle)


# In[4]:


# Print the object attribute radius

RedCircle.radius


# In[5]:


# Print the object attribute color

RedCircle.color


# In[6]:


# Set the object attribute radius

RedCircle.radius = 1
RedCircle.radius


# In[10]:


# Import the library

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


# Call the method drawCircle

RedCircle.drawCircle()


# In[12]:


# Use method to change the object attribute radius

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


# In[13]:


# Create a blue circle with a given radius

BlueCircle = Circle(radius=100)


# In[14]:


# Print the object attribute radius

BlueCircle.radius


# In[15]:


# Print the object attribute color

BlueCircle.color


# In[16]:


# Call the method drawCircle

BlueCircle.drawCircle()


# In[17]:


# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()


# In[18]:


# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 10, 'blue')


# In[19]:


# Print the object attribute height

SkinnyBlueRectangle.height 


# In[20]:


# Print the object attribute width

SkinnyBlueRectangle.width


# In[21]:


# Print the object attribute color

SkinnyBlueRectangle.color


# In[22]:


# Create a new object rectangle

FatYellowRectangle = Rectangle(20, 5, 'yellow')


# In[23]:


# Print the object attribute width

FatYellowRectangle.width


# In[24]:


# Print the object attribute height

FatYellowRectangle.height 


# In[25]:


# Use the drawRectangle method to draw the shape

FatYellowRectangle.drawRectangle()

