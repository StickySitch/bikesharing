#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# 1. Create a DataFrame for the 201908-citibike-tripdata data. 
data = pd.read_csv('201908-citibike-tripdata.csv')


# In[3]:


# 2. Check the datatypes of your columns. 
data.dtypes


# In[5]:


# 3. Convert the 'tripduration' column to datetime datatype.

# Adding "Trip duration DT" column by copying the "tripduration" column. (DT = DateTime)
data['trip duration DT'] = data['tripduration']

# Converting 'trip duration DT' seconds values to a date and time format
data['trip duration DT'] = pd.to_datetime(data['trip duration DT'], unit='s')
data.head(10)


# In[9]:


# Moving trip duration DT to the first column
cols = list(data.columns)
cols = [cols[-1]] + cols[:-1]
data = data[cols]
data.head(10)


# In[7]:


# 4. Check the datatypes of your columns. 
data.dtypes


# In[10]:


# 5. Export the Dataframe as a new CSV file without the index.
data.to_csv('201908-citibike-tripdata-converted.csv', index=False)


# In[ ]:




