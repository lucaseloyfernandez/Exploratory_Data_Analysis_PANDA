#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv(r"C:\Users\lucas\Desktop\Programacion 2019\Phyton\Exploratory Data Analysis in Pandas\world_population.csv")
df


# In[5]:


# HERE WE CHANGE THE SCIENTIFIC VALUE OF THE NUMBERS FROM .0 TO .00
pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[49]:


# HERE WE CAN SEE WHAT DATA TYPE VALUES HAS THE DATA SET
df.select_dtypes(include='object')
df.select_dtypes(include='float')


# In[7]:


# THE INFO() FUNCTION SHOW US DATA ABOUT THE DATA SET WE ARE EXPLORING
df.info()


# In[9]:


# THE DESCRIBE() FUNCTION SHOW US MORE INFO OF THE DATA SET
df.describe()


# In[11]:


# THE ISNULL() FUNCTION SHOW US IF THERE IS ANY NULL VALUES IN THE DATASET
df.isnull().sum()


# In[13]:


# THE NUNIQUE() FUNCTION SHOW US HOW MANY UNIQUE VALUES THERE ARE IN THE DATASET.
df.nunique()


# In[15]:


# THE SORT() FUNCTION SORT THE VALUES OF THE DATA WE WANT
df.sort_values(by="World Population Percentage", ascending=False).head(10)


# In[21]:


# THE CORR() FUNCTION SHOW US THE CORRELETAION BETWEEN COLUMNS, THE CORRELATION IS 1:1
df.corr(numeric_only = True)


# In[25]:


# NOW WE CREAT A HEATMAP OF THE CORRELATION 
sns.heatmap(df.corr (numeric_only=True) , annot = True)
plt.rcParams['figure.figsize'] = (20,7)
plt.show()


# In[29]:


# WE GROUP BY CONTINENT
df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)


# In[31]:


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
df2


# In[33]:


df3 = df2.transpose()
df3


# In[35]:


# NOW WE VISUALIZE THE POPULATION GROWTH OF THE CONTINENTS BY YEAR
df3.plot()


# In[37]:


df.boxplot(figsize=(20,10))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




