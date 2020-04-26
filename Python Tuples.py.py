
# coding: utf-8

# In[1]:


# Create your first tuple

tuple1 = ("disco",10,1.2 )
tuple1


# In[2]:


# Print the type of the tuple you created

type(tuple1)


# In[3]:


# Print the variable on each index

print(tuple1[0])
print(tuple1[1])
print(tuple1[2])


# In[4]:


# Print the type of value on each index

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))


# In[5]:


# Use negative index to get the value of the last element

tuple1[-1]


# In[6]:


# Use negative index to get the value of the second last element

tuple1[-2]


# In[7]:


# Use negative index to get the value of the third last element

tuple1[-3]


# In[8]:


# Concatenate two tuples

tuple2 = tuple1 + ("hard rock", 10)
tuple2


# In[9]:


# Slice from index 0 to index 2

tuple2[0:3]


# In[10]:


# Slice from index 3 to index 4

tuple2[3:5]


# In[11]:


# Get the length of tuple

len(tuple2)


# In[12]:


#Sorting


# A sample tuple
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)


# In[13]:


# Sort the tuple

RatingsSorted = sorted(Ratings)
RatingsSorted


# In[14]:


# Create a nest tuple

NestedT =(1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))


# In[15]:


# Print element on each index

print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])


# In[16]:


# Print element on each index, including nest indexes

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])


# In[17]:


# Print the first element in the second nested tuples

NestedT[2][1][0]


# In[18]:


# Print the second element in the second nested tuples

NestedT[2][1][1]


# In[19]:


# sample tuple

genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock",                 "R&B", "progressive rock", "disco") 
genres_tuple


# In[20]:


len(genres_tuple)#len(genres_tuple)


# In[21]:


genres_tuple[3] #accesing the third element

