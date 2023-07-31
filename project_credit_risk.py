# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


#Credit risk database
base_credit = pd.read_csv('data/credit_data.csv')                           

#Data exploration

## displays the first records ​​of the table, in the argument you must input the value of the quantities to be shown
base_credit.head(10)

## displays the last records ​​of the table, in the argument you must input the value of the quantities to be shown
base_credit.tail(10)

## display the statistic data
base_credit.describe()

## returns the record of the person with the highest salary
base_credit[base_credit['income'] >= 69995.685578  ]

## returns the record of the person with the smallest debt
base_credit[base_credit['loan'] <= 1.377630]

#Data display

## count of records in each class
np.unique(base_credit['default'], return_counts=True)

## count graphic display
sns.countplot(x = base_credit['default']);
plt.hist(x = base_credit['age']);
plt.hist(x = base_credit['income']);
plt.hist(x = base_credit['loan']);

graphic = px.scatter_matrix(base_credit, dimensions=['age','income'])
graphic.show()

