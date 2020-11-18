#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd 
import numpy as np 
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt 


# In[52]:


data=pd.read_csv("911.csv")


# In[53]:



data


# In[4]:


data.info()


# In[5]:


data.isnull().sum().sort_values(ascending=False)


# In[6]:


#### a.What are the top 5 zipcodes for 911 calls?


# In[7]:


data['zip'].value_counts().head()


# In[8]:


### b.What are the top 5 townships (twp) for 911 calls?


# In[9]:


data['twp'].value_counts().head()


# In[10]:


### c.Take a look at the 'title' column, how many unique title codes are there?


# In[11]:


data['title'].nunique
#count(distinct title)


# In[12]:


### d.In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value


# In[13]:


data['Reason']=data['title'].apply(lambda title:title.split(':')[0])

data.head()
# In[14]:


### e. What is the most common Reason for a 911 call based off of this new column?


# In[15]:


data['Reason'].value_counts()


# In[16]:


### a.Now use seaborn to create a countplot of 911 calls by Reason


# In[17]:


sns.countplot(x ='Reason', data =data)  


# In[18]:


## b. Use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.


# In[19]:


type(data['timeStamp'].iloc[0])


# In[20]:


## form above obserbation  we  see that timeStamp is str data type so  for performing the task B we  have to do some  data cleaning operation 


# In[21]:


data['timeStamp']=pd.to_datetime(data['timeStamp'])


# In[22]:


type(data['timeStamp'].iloc[0])


# In[23]:


time = data['timeStamp'].iloc[0]
time.hour


# In[24]:


data['Hour'] = data['timeStamp'].apply(lambda time:time.hour)
data['Month'] = data['timeStamp'].apply(lambda time:time.month)
data['Day of Week'] = data['timeStamp'].apply(lambda time:time.dayofweek)


# In[25]:


data.head(1)


# In[26]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[27]:


data['Day of Week'] = data['Day of Week'].apply(lambda int:dmap[int])


# In[28]:


### Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.


# In[29]:


sns.countplot(x='Day of Week', hue='Reason', data=data)


# In[30]:


sns.countplot(x='Month', hue='Reason', data=data)


# In[31]:


## d Compare the result from b and c


# In[32]:


""" it was missing some months. Let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas..."""


# In[33]:


byMonth = data.groupby(by='Month').count()


# In[34]:


byMonth


# In[35]:


### e Create a simple plot off of the dataframe indicating the count of calls per month. 


# In[36]:


byMonth['lat'].plot()


# In[37]:


# f. Use seaborn's lmplot() to create a linear fit on the number of calls per month


# In[38]:


sns.pointplot(x=byMonth.index, y = 'lat', data=byMonth, markers='.')


# In[39]:


# g Create a new column called 'Date' that contains the date from the timeStamp column. 


# In[40]:


data['Date'] = data['timeStamp'].apply(lambda time:time.date())


# In[41]:


data.head(2)


# In[42]:


#h.Groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.


# In[43]:


data.groupby(by='Date').count()['lat'].plot()


# In[44]:


### i.Recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call


# In[45]:


data[data['Reason']=='Fire'].groupby(by='Date').count()['lat'].plot()
plt.title('Fire')


# In[46]:


data[data['Reason']=='Traffic'].groupby(by='Date').count()['lat'].plot()
plt.title('Traffic')


# In[47]:


data[data['Reason']=='EMS'].groupby(by='Date').count()['lat'].plot()
plt.title('EMS')


# In[48]:


## j.Heatmaps – Try to explore all the possibilities of different heatmap and create those. Once you create heatmaps, you should analyse the output. 


# In[ ]:





# In[ ]:




