# -*- coding: utf-8 -*-
"""Sales Prediction Using Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13C9N9qAkJavFAGxdiFaSi25_wdb5CDK_
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy import stats
import pylab
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline
sns.set(style="darkgrid", font_scale=1.5)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error,mean_absolute_percentage_error

df=pd.read_csv("/content/Advertising.csv")
df

df.drop(['Unnamed: 0'], axis=1, inplace=True)

df.head()

df.tail()

print("Dimensions of the dataset are: ", df.shape)

df.columns

df.info()

df.describe()

df.shape

df.info()

df.isnull().sum()

df[df.duplicated()].any()

df.corr()

"""Data Visualization"""

plt.figure(figsize=(15,6))

plt.subplot(1,2,1)
sns.histplot(df["Sales"], color="maroon", kde=True)
plt.title("Sales Feature Distribution", fontweight="black", pad=20, fontsize=20)

plt.subplot(1,2,2)

stats.probplot(df[ "Sales"],dist="norm", plot=pylab)
plt.show()

df.hist(bins=60)
plt.show()

df.describe(include='all')

df.duplicated().sum()

import plotly.express as px
fig = px.scatter(df, x="TV", y="Newspaper", color="Sales", size="Radio", hover_data=["Sales"])
fig.show()

fig=px.box(df, y="Sales")
fig.show()
fig=px.box(df["TV"])
fig.show()
fig=px.box(df[ "Radio"])
fig.show()
fig=px.box(df["Newspaper"])
fig.show()

# Checking the Coorelation of Features
plt.figure(figsize=(20,6))
sns.heatmap(df.corr(), annot=True,cmap="summer")
plt.title("Coorelation among The Features",fontweight="black",fontsize=24,pad=22)
plt.show()

y.head()

y.tail()

px.scatter(df,x= 'Radio',y='Sales', width=700, height=400, title='Sale Vs Radio')

px.scatter(df,x= 'Radio',y='Sales', width=700, height=400, title='Radio Vs TV')

px.scatter(df,x= 'TV',y='Sales', width=700, height=400, title='Sale Vs TV')

px.scatter(df,x= 'Newspaper',y='Sales', width=700, height=400, title='Sale Vs Newspaper')

px.scatter(df,x= 'TV',y='Sales', width=700, height=400, title='TV Vs Newspaper')



px.scatter(df,x= 'Newspaper',y='Sales', width=700, height=400, title=' Newspaper Vs Radio')

X = df.drop('Sales', axis = 1)
y=df['Sales']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(X_train,y_train)

print("intercep", lr.intercept_)
print("coefficents: ")
list(zip(X,lr.coef_))

y_pred = lr.predict(X_test)
print("prediction{}".format(y_pred))

lr_dif=pd.DataFrame({"ir": y_test, "coe": y_pred})

lr_dif.head()

from sklearn.metrics import r2_score
r2_score(y_test, y_pred)