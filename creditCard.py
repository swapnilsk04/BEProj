#!/usr/bin/env python
# coding: utf-8

# In[4]:


import json
data = json.loads(open('/home/jayesh/Desktop/1.json').read())
data


# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.DataFrame(data)
df


# In[7]:


X = df[['card number']]
y = df['mac id']
plt.scatter(X,y)


# In[8]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)


# In[12]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression().fit(X_train, y_train)


# In[13]:


clf.score(X_test, y_test)

