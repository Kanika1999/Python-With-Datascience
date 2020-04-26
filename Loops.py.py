
# coding: utf-8

# In[1]:


"""What is for loop?
The for loop enables you to execute a code block multiple times. For example, you would use this if you would like to print out every element in a list.
Let's try to use a for loop to print all the years presented in the list dates:

This can be done as follows:
"""
# For loop example

dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])  


# In[2]:


# Example of for loop

for i in range(0, 8):
    print(i)


# In[3]:


# Exmaple of for loop, loop through list

for year in dates:  
    print(year)   


# In[4]:


# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'weight'
    print("After square ", i, 'is',  squares[i])


# In[5]:


# Loop through the list and iterate on both index and element value

squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)


# In[6]:


"""What is while loop?
As you can see, the for loop is used for a controlled flow of repetition. 
However, what if we don't know when we want to stop the loop? What if we want to keep 
executing a code block until a certain condition is met? The while loop exists as a tool for
repeated execution based on a condition.
The code block will keep being executed until the given logical condition 
returns a False boolean value.
"""
# While Loop Example

dates = [1982, 1980, 1973, 2000]

i = 0
year = 0

while(year != 1973):
    year = dates[i]
    i = i + 1
    print(year)

print("It took ", i ,"repetitions to get out of loop.")


# In[7]:


#Write a for loop the prints out all the element between -5 and 5 using the range function.

# Write your code below and press Shift+Enter to execute
for i in range(-5,6):
    print(i)


# In[8]:


#Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.

# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)


# In[9]:


#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

# Write your code below and press Shift+Enter to execute

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)


# In[10]:


#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=1
rating= PlayListRatings[0]
while(rating>=6):
    print(rating)
    rating=PlayListRatings[i]
    i=i+1

