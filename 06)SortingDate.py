#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10,6


# In[32]:


df = pd.read_csv(r"C:\Users\91783\Desktop\TSA\Data1.csv")


# In[33]:


df.head(40)


# In[34]:


df["Date"] = pd.to_datetime(df["Date"])
print(df.dtypes)


# In[35]:


df.head(40)


# In[36]:


df.sort_values(by='Date', inplace=True)
print(df)


# In[44]:


df.head(60)


# In[ ]:




