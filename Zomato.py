# -*- coding: utf-8 -*-
"""project zomato.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15gRwloAvHwVrQUP_gvpLy3P01YMfDx_5
"""

## 1 Importing the libraries###
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## 2 Reading the csv file using pandas##
import pandas as pd
df = pd.read_csv('/content/zomato.csv',error_bad_lines=False,engine="python")

df

df.head()

df.shape

## 3 How many columns are there in the data set####
df.columns

## 4 Removing the data set which are not use full for us or private data##
df1 = df.drop(['url','address','phone','menu_item','dish_liked','reviews_list'],axis = 1)
df1

## 5 How many null values are present in our dataset###
df1.info()

## 6 There are many duplicates values present in our dataset we have to remove them for proper cleaning of data##
df1.drop_duplicates(inplace = True)
df1

#### cleaing of dataset ####

## 7 Frist lets clean the rate column because it has the fractional values####

## 8 Let us frist check how unique values are present in the rate column ##
df1['rate'].unique()

## there are some values like NEW,NAN and also i want remove "/5"###

import numpy as np
def handel(value):
  if(value=='NEW' or value=='-'):
    return np.nan
  else:
    value = str(value).split('/')
    value = value[0]
    return float(value)

df1['rate'] = df1['rate'].apply(handel)
df1['rate']

df1.info()

## as we can there null values present in rate,rest_type,approx_cost column
## 9 now lets remove the null values present in rate column###

## lets check how many null vales are present the rate column##

df1.rate.isnull().sum()

df1['rate'].fillna(df1['rate'].mean(),inplace = True)
df1

## 10 there are some null values present in other columns soo lets drop them and moev forward##

df1.dropna(inplace = True)
df1

## 11 now lets change some columns name that have lenght name###

df1.rename(columns = {'approx_cost(for two people)': 'cost2plates','listed_in(type)':'Type'},inplace = True)
df1

### 12 since the loacation and listed_in(city) contains the same information lets remove one of them###

df1 = df1.drop(['listed_in(city)'],axis = 1)
df1

## we have almost cleaned the dataset now lets go to visualization##

###  DATA VISUALIZATION ##

## 13 lets plot a count for various loctions by which we can get an idea which locations has more number of resturants##

plt.figure(figsize = (16,10))
ax = sns.countplot(df1['location'])
plt.xticks(rotation = 90)  ### by using these llines we get row values in 90 degree line##

## 14  Now lets get the  data how many restaurants have online order facility? ###

plt.figure(figsize = (6,6))
sns.countplot(df['online_order'],palette = 'inferno')

## 15  Now lets get the  data how many restaurants have book table facility? ###

plt.figure(figsize = (6,6))
sns.countplot(df['book_table'],palette = 'rainbow')

###  16 now lets check the restaurants which have online order facility and there rating given by user?###

plt.figure(figsize = (6,5))
sns.boxplot(x= 'online_order',y = 'rate',data = df1)

### the resrt having online order facilate have rating near 4 but the rest have not having online order facility is round 3.5 as we can see in the box plot analysis###1

### 17 now lets check the same rating according to book table information

plt.figure(figsize = (6,5))
sns.boxplot(x= 'book_table',y = 'rate',data = df1)

### as we can see there huge differnce in rating given by the people between book table on online order facility

## 18 now lets create some pivot table by using location and online order facility which we easy our visualization

df2 = df1.groupby(['location','online_order'])['name'].count()
df2.to_csv('location_online.csv')
df2 = pd.read_csv('location_online.csv')
df2 = pd.pivot_table(df2,values=None,index=['location'],columns=['online_order'],fill_value=0,aggfunc=np.sum)
df2

df2.plot(kind = 'bar', figsize = (15,8))

### oraange shows number restaurants that gives online order facility

## blue shows number of restaurants that doesn't provide online facility

## 19 now lets visualize restaurenst based on rating

plt.figure(figsize = (14,8))
sns.boxplot(x = 'Type', y = 'rate',data = df1 ,palette = 'inferno')

### as we can see the maximum restuarents rating is given to drinks and nightlife

