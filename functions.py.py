
# coding: utf-8

# In[1]:


"""Functions
A function is a reusable block of code which performs operations specified in the function. They let you break down tasks and allow you to reuse your code in different programs.

There are two types of functions :

Pre-defined functions
User defined functions
What is a Function?
You can define functions to provide the required functionality. Here are simple rules to define a function in Python:

Functions blocks begin def followed by the function name and parentheses ().
There are input parameters or arguments that should be placed within these parentheses.
You can also define parameters inside these parentheses.
There is a body within every function that starts with a colon (:) and is indented.
You can also place documentation before the body
The statement return exits a function, optionally passing back a value
An example of a function that adds on to the parameter a prints and returns the output as b:
"""
#First function example: Add 1 to a and store as b

def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return(b)


# In[2]:


# Get a help on add function

help(add)


# In[3]:


# Call the function add()

add(1)


# In[4]:


# Call the function add()

add(2)


# In[5]:


# Define a function for multiple two numbers

def Mult(a, b):
    c = a * b
    return(c)


# In[6]:


# Use mult() multiply two integers

Mult(2, 3)


# In[7]:


"""Variables
The input to a function is called a formal parameter.

A variable that is declared inside a function is called a local variable. The parameter only exists within the function (i.e. the point where the function starts and stops).

A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program. We will discuss more about global variables at the end of the lab.
"""
# Function Definition

def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


# In[8]:


# Initializes Global variable  

x = 3
# Makes function call and return function a y
y = square(x)
y


# In[9]:


# Directly enter a number as parameter

square(2)


# In[10]:


# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)


# In[11]:


# See the output

MJ()


# In[12]:


# See what functions returns are

print(MJ())
print(MJ1())


# In[13]:


# Define the function for combining strings

def con(a, b):
    return(a + b)


# In[14]:


# Test on the con() function

con("This ", "is")


# In[15]:



def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 


# In[16]:


a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1


# In[17]:


# Build-in function print()

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)


# In[18]:


# Use sum() to add every element in a list or tuple together

sum(album_ratings)


# In[19]:


# Show the length of the list or tuple

len(album_ratings)


# In[20]:


# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# In[21]:


# Print the list using for loop

def PrintList(the_list):
    for element in the_list:
        print(element)


# In[22]:


# Implement the printlist function

PrintList(['1', 1, 'the man', "abc"])


# In[24]:


# Example for setting param with default value

def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

        


# In[25]:


# Test the value with default value and with input

isGoodRating()
isGoodRating(10)


# In[26]:


# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var = artist
    print(artist, "is an artist")
    
printer1(artist)


# In[27]:


artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)


# In[29]:


# Example of global variable

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)


# In[30]:


# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)


# In[31]:


# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)

