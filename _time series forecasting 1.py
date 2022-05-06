#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.pyplot import rcParams
rcParams ['figure.figsize']=10,6


# In[3]:


# importing data file
dataset=pd.read_csv("AirPassengers.csv")
dataset.head(5)


# In[9]:


# convert data into datewise format
dataset['Month']=pd.to_datetime(dataset['Month'],infer_datetime_format=True)
indexedDataset=dataset.set_index(["Month"])


# In[10]:


# INDEX data from firstdate to lastdate
from datetime import datetime
indexedDataset.head()


# In[11]:


# always firsttask in timeseries forecasting is to plot the data
plt.xlabel("Date") 
plt.ylabel("No of Air Passengers")
plt.plot(indexedDataset)


# In[13]:


# findout rolling mean and standard deviation
rolmean=indexedDataset.rolling(window=12).mean()
rolstd=indexedDataset.rolling(window=12).std()
print(rolmean,rolstd)


# In[14]:


#display rolling mean and standard deviation along with original data - always 3rd step in TS
Ori=plt.plot(indexedDataset,color='blue',label='Original')
mean=plt.plot(rolmean,color='red',label='Rolling Mean')
std=plt.plot(rolstd,color='black',label='Rolling Std')
plt.legend(loc="best")
plt.title("Rolling Mean and Standard Deviation")
plt.show(block=False)


# In[17]:


# Perform Dicky Fuller Test (Unitroot test used to check stationarity of the data) Always 4th Step
from statsmodels.tsa.stattools import adfuller
print("Results of Dicky-Fuller Test:")
dftest=adfuller(indexedDataset["#Passengers"],autolag='AIC')
dfoutput=pd.Series(dftest[0:4],index=['test Statistic','p value','#Lags Used','Number of Observations Used'])
for key,value in dftest[4].items():
    dfoutput['Critical value (%s)'%key]=value
print(dfoutput)
# Ho = the time series data is non stationary
# As the p value is more than 0.05 , we accept the null hypothesis and can say that the TSD is non stationar


# In[ ]:


indexDataset_logscale=np.log(indexedDataset)
plt.plot

