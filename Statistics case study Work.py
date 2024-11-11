#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install numpy


# In[5]:


pip install seaborn


# In[1]:


pip install pandas


# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns


# # Measure of Central Tendency
# #calculate the mean, median and mode of the following
# MCT =[5, 7, 2, 8, 5, 3, 7]

# In[116]:


MCT =[5, 7, 2, 8, 5, 3, 7]


# In[8]:


import statistics


# In[10]:


print(statistics.mean(MCT))


# In[12]:


print(statistics.median(MCT))


# In[14]:


print(statistics.mode(MCT))


# In[16]:


#Measure of Dispersion


# In[19]:


import pandas as pd
MOD=(12,15,18,22,25)
mydata=pd.DataFrame(MOD)
summary=mydata.describe()
summary=pd.DataFrame(summary)
summary=round(summary,2)
summary.columns=["Item"]
print(summary)


# In[21]:


import warnings
warnings.filterwarnings("ignore")
Range=summary.Item[7]-summary.Item[3]
print("Range=" ,Range)
Q3=summary.Item[6]
print("Quartile3" ,Q3)
Q1=summary.Item[4]
print("Quartile1=" ,Q1)
IQR=Q3-Q1
print("InterQuartileRange=" , IQR)



# In[24]:


#OUtlier Detetion
##identifying an outlier using IQR



# In[26]:


OD = [17,20, 21, 18, 95, 22, 19, 23]
sort_OD = np.sort(OD)
sort_OD


# In[27]:


#Calculte the Q1, Q2,Q3 and IQR
Q1 = np.percentile(OD, 25, interpolation = 'midpoint')
Q2 = np.percentile(OD, 50, interpolation = 'midpoint')
Q3 = np.percentile(OD, 75, interpolation = 'midpoint')


# In[28]:


print('Q1 25 percentile of the given OD is, ', Q1)
print('Q1 50 percentile of the given OD is, ', Q2)
print('Q1 75 percentile of the given OD is, ', Q3)


# In[30]:


IQR = Q3-Q1
print('interquartile range is', IQR)


# In[31]:


# following code can also be use to calculate the IQR
from scipy import stats

IQR_with_scipy=stats.iqr(OD, interpolation = 'midpoint')
IQR_with_scipy


# In[33]:


#Finding the lower and upper limits as Q1-1.5 IQR and Q3+1.5 IQR, respectively
low_lim = Q1-1.5*IQR
up_lim =Q3+1.5*IQR
print('low_limit is', low_lim)
print('up_limit is', up_lim)


# In[35]:


sns.boxplot(OD);


# In[37]:


#Normal Distribution and Z-Scores
## A population has a mean of 75 and a standard deviation of 10. calculate the Z-score foe a value 85



# In[39]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[95]:


x =np.random.normal(75,10,85)


# In[98]:


x ={'Data' :np.random.normal(75,10,85)}
df =pd.DataFrame(x)


# In[99]:


print(df)


# In[100]:


df.head()


# In[101]:


df.mean()


# In[103]:


df.std()


# In[104]:


upper_limit =df.mean() +10*df.std()
upper_limit


# In[106]:


lower_limit = df.mean() -10*df.std()
lower_limit


# In[108]:


df.max()


# In[110]:


#Using displot 
sns.displot(df, kde=True, rug=True);


# In[112]:


#using Boxplot
sns.boxplot(df);


# In[114]:


df.describe()


# In[117]:


# The Z_SCORE FOR 85 VALUE
df_no_outlier_std_dev =df[(df<upper_limit) & (df>lower_limit)]
df_no_outlier_std_dev.shape


# In[118]:


#Covarian and correlation
##calculate the covarian and  correlation coefficient between two variable x a nd y with the following data
x :[15, 20, 25, 30, 35]
y: [10, 18, 22, 28, 40]


# In[123]:


xs ={'1st Data': [15, 20, 25, 30, 35]}
XS = pd.DataFrame(xs)
print(XS)


# In[128]:


YS = {'2nd Data': [10, 18, 22, 28, 40]}
YS = pd.DataFrame(YS)
print(YS)


# In[131]:


XS.corr()


# In[133]:


YS.corr()


# In[135]:


XS,YS.corr()


# In[207]:


YS,XS.corr()


# In[197]:


pearsonr(XS['1st Data'], y =YS ['2nd Data'])


# In[208]:


sns.rugplot(x = XS["1st Data"], y= YS["2nd Data"], color='red')
plt.show()


# In[211]:


sns.regplot(x = XS["1st Data"], y= YS["2nd Data"], color='blue')
plt.show()


# In[214]:


sns.scatterplot(x = XS["1st Data"], y= YS["2nd Data"], color='red')
plt.title('The Correlation ')
plt.show()


# In[ ]:


## THANK YOU JUPITA ACADEMY!

