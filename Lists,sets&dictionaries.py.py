
# coding: utf-8

# In[1]:


# Create a list

L = ["Michael Jackson", 10.1, 1982]
L


# In[2]:


# Print the elements on each index

print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# In[3]:


# Sample List

L = ["Michael Jackson", 10.1,1982,"MJ",1]
L


# In[4]:


# List slicing

L[3:5]


# In[5]:


# Use extend to add elements to list

L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L


# In[6]:


# Use append to add elements to list

L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L


# In[7]:


# Use append to add elements to list

L.append(['a','b'])
L


# In[8]:


# Change the element based on the index

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)


# In[9]:


# Delete the element based on the index

print('Before change:', A)
del(A[0])
print('After change:', A)


# In[10]:


# Split the string, default is by space

'hard rock'.split()


# In[11]:


# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)


# In[12]:


# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])


# In[13]:


# Clone (clone by value) the list A

B = A[:]
B


# In[14]:


print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])


# In[15]:


# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1


# In[16]:


# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19",               "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set


# In[17]:


# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",                     "progressive rock", "soft rock", "R&B", "disco"])
music_genres


# In[18]:


# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
A


# In[19]:


# Add element to set

A.add("NSYNC")
A


# In[20]:


# Try to add duplicate element to the set

A.add("NSYNC")
A


# In[21]:


# Remove the element from set

A.remove("NSYNC")
A


# In[22]:


# Verify if the element is in the set

"AC/DC" in A


# In[23]:


# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])


# In[24]:


# Print two sets

album_set1, album_set2


# In[25]:


# Find the intersections

intersection = album_set1 & album_set2
intersection


# In[26]:


# Find the difference in set1 but not set2

album_set1.difference(album_set2)  


# In[28]:


#Use intersection method to find the intersection of album_list1 and album_list2

album_set1.intersection(album_set2)   


# In[29]:


album_set1.union(album_set2) #for union method


# In[30]:


# Check if superset

set(album_set1).issuperset(album_set2)   


# In[31]:


# Check if subset

set(album_set2).issubset(album_set1)     


# In[32]:


# Check if subset

set({"Back in Black", "AC/DC"}).issubset(album_set1) 


# In[34]:


# Create the dictionary

Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 6}
Dict


# In[35]:


# Access to the value by the key

Dict["key1"]


# In[36]:


# Access to the value by the key

Dict[(0, 1)]


# In[37]:


# Create a sample dictionary

release_year_dict = {"Thriller": "1982", "Back in Black": "1980",                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",                     "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


# In[38]:


# Get value by keys

release_year_dict['Thriller'] 


# In[39]:


# Get value by key

release_year_dict['The Bodyguard'] 


# In[40]:


# Get all the keys in dictionary

release_year_dict.keys() 


# In[41]:


# Get all the values in dictionary

release_year_dict.values() 


# In[42]:


# Append value with key into dictionary

release_year_dict['Graduation'] = '2007'
release_year_dict


# In[43]:


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# In[44]:


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict

