
# coding: utf-8

# In[1]:


"""Condition Statements
Comparison Operators
Comparison operations compare some value or operand and, based on a condition, 
they produce a Boolean. When comparing two values you can use these operators:
equal: ==
not equal: !=
greater than: >
less than: <
greater than or equal to: >=
less than or equal to: <=
Let's assign a a value of 5. Use the equality operator denoted with two equal == signs to determine if two values are equal.
The case below compares the variable a with 6.

"""
# Condition Equal

a = 5
a == 6


# In[2]:


# Greater than Sign

i = 6
i > 5


# In[3]:


# Greater than Sign

i = 2
i > 5


# In[4]:


# Inequality Sign

i = 6
i != 6


# In[5]:


# Use Equality sign to compare the strings

"ACDC" == "Michael Jackson"


# In[6]:


# Use Inequality sign to compare the strings

"ACDC" != "Michael Jackson"


# In[7]:


# Compare characters

'BA' > 'AB'


# In[8]:


"""
Branching
Branching allows us to run different statements for different inputs. It is helpful to think of an if statement as a locked room, if the statement is True we can enter the room and your program will run some predefined tasks, but if the statement is False the program will ignore the task.

For example, consider the blue rectangle representing an ACDC concert. If the individual is older than 18, they can enter the ACDC concert. If they are 18 or younger than 18 they cannot enter the concert.

Use the condition statements learned before as the conditions need to be checked in the if statement. The syntax is as simple as  if condition statement :, which contains a word if, any condition statement, and a colon at the end. Start your tasks which need to be executed under this condition in a new line with an indent. The lines of code after the colon and with an indent will only be executed when the if statement is True. The tasks will end when the line of code does not contain the indent.

In the case below, the tasks executed print(“you can enter”) only occurs if the variable age is greater than 18 is a True case because this line of code has the indent. However, the execution of print(“move on”) will not be influenced by the if statement.
"""
# If statement example

age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# In[9]:


# Else statement example

age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# In[10]:


# Elif statment example

age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# In[11]:


# Condition statement example

album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# In[12]:


# Condition statement example

album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')


# In[13]:


#logical operators

#and
#or
#not

# Condition statement example

album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# In[14]:


# Condition statement example

album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# In[15]:


# Condition statement example

album_year = 1983

if not (album_year == '1984'):
    print ("Album year is not 1984")

