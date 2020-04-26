
# coding: utf-8

# In[1]:


# Use quotation marks for defining string

"Michael Jackson"


# In[2]:


# Use single quotation marks for defining string

'Michael Jackson'


# In[4]:


#A string can be a combination of spaces and digits:

# Digitals and spaces in string

'1 2 3 4 5 6 '


# In[5]:


#A string can also be a combination of special characters :

# Special characters in string

'@#2_#]&*^%$'


# In[6]:


#We can print our string using the print statement:

# Print the string

print("hello!")


# In[7]:


#We can bind or assign a string to another variable:

# Assign string to variable

Name = "Michael Jackson"
Name


# In[8]:


#INDEXING OF STRINGS
# Print the first element in the string

print(Name[0])


# In[9]:


# Print the element on index 6 in the string

print(Name[6])


# In[10]:


# Print the element on the 13th index in the string

print(Name[13])


# In[11]:


#NEGATIVE INDEXING
# Print the last element in the string

print(Name[-1])


# In[12]:


# Print the first element in the string

print(Name[-15])


# In[13]:


# Find the length of string

len("Michael Jackson")


# In[14]:


#SLICING
# Take the slice on variable Name with only index 0 to index 3

Name[0:4]


# In[15]:


# Take the slice on variable Name with only index 8 to index 11

Name[8:12]


# In[16]:


# Get every second element. The elments on index 1, 3, 5 ...

Name[::2]


# In[17]:


# Get every second element in the range from index 0 to index 4

Name[0:5:2]


# In[18]:


# Concatenate two strings

Statement = Name + "is the best"
Statement


# In[19]:


# Print the string for 3 times

3 * "Michael Jackson"


# In[20]:


# Concatenate strings

Name = "Michael Jackson"
Name = Name + " is the best"
Name


# In[21]:


# New line escape sequence

print(" Michael Jackson \n is the best" )


# In[22]:


#Tab escape sequence

print(" Michael Jackson \t is the best" )


# In[23]:


# Include back slash in string

print(" Michael Jackson \\ is the best" )


# In[24]:


# r will tell python that string will be display as raw string

print(r" Michael Jackson \ is the best" )


# In[25]:


#STRING OPERATION
# Convert all the characters in string to upper case

A = "Thriller is the sixth studio album"
print("before upper:", A)
B = A.upper()
print("After upper:", B)


# In[26]:


# Replace the old substring with the new target substring is
#the segment has been found in the string

A = "Michael Jackson is the best"
B = A.replace('Michael', 'Janet')
B


# In[27]:


# Find the substring in the string. Only the index of the first elment of substring in string will be the output

Name = "Michael Jackson"
Name.find('el')


# In[28]:


# Find the substring in the string.

Name.find('Jack')


# In[29]:


# If cannot find the substring in the string

Name.find('Jasdfasdasdf')


# In[30]:


#Consider the variable G, and find the first index of the sub-string snow:

# Write your code below and press Shift+Enter to execute

G = "Mary had a little lamb Little lamb, little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
G.find("snow")

