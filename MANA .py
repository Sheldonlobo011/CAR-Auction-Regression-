#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import statsmodels.api as sm


# In[8]:


data = pd.read_csv('ABC auctions.csv')


# In[9]:


# Define the dependent and independent variables
y = data['earningspct']
X = data[['legacy', 'sold','ftturn', 
          'ptturn', 'ohsapercar', 
          'lotdampercar']]


# In[10]:


# Check for multicollinearity among the independent variables
corr_matrix = X.corr()
print(corr_matrix)


# In[12]:


# Run a multiple regression model FIRST REGESSION 
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[14]:


second regression 


# In[15]:


# Step 2: Define the dependent and independent variables
y = data['ftturn']
X = data[['legacy','sold','ei', 'oc']]


# In[16]:


# Step 4: Run a multiple regression model
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[ ]:


REGRESSION 3 


# In[17]:


# Step 2: Define the dependent and independent variables
y = data['ohsapercar']
X = data[['legacy','sold','ei', 'oc']]


# In[18]:


# Step 2: Define the dependent and independent variables
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())


# In[ ]:


REGESSIOIN 4 


# In[20]:


# Step 2: Define the dependent and independent variables
y = data['lotdampercar']
X = data[['legacy','sold','ei', 'oc']]


# In[21]:


# Step 2: Define the dependent and independent variables
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print(model.summary())

