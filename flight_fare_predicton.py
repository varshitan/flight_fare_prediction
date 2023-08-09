import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Importing the training dataset
train_data = pd.read_excel('Data_Train.xlsx')

# Display the first 10 rows of the dataset
print(train_data.head(10))

# Describe function provides statistical information about the given data
print(train_data.describe())

# Next step is to clean all the data (i.e., handle any missing values)

# To find any missing values present in the data, we use the info method
print(train_data.info())

# The info method returns non-null counts and data types

# If we observe the output, there is a slight change in the values of 'Route' and 'Total_Stops'

# The isnull method converts everything into boolean type (True or False) to indicate null values
print(train_data.isnull())

# It gives the sum of null values in each column in the dataset
print(train_data.isnull().sum())

# From the results, we can observe that the columns 'Route' and 'Total_Stops' have 1 null value each

# To get information about those rows which contain null data in the 'Total_Stops' column
print(train_data[train_data['Total_Stops'].isnull()])

# To get information about those rows which contain null data in the 'Route' column
print(train_data[train_data['Route'].isnull()])

# Since this dataset contains a small number of null values, we can drop both rows with null values (DATA CLEANING)
train_data.dropna(inplace=True)

# Now the dataset has been cleaned by dropping rows with null values
# creating a copy of this data so maupulations can be doneon the other dataset

data =train_data.copy()
# changing the datatype to datetime since machine cannot understand the object type 
# instead of writing long codes we define a function because whenever there is a repititon of data its better to defne a function 
def change_into_datetime(col):
    data[col] = pd.to_datetime(data[col], dayfirst=True)
# giving all the feaures that needs to convert in a list and then caling chage_into_datetime function
for feature in ['Dep_Time', 'Arrival_Time' , 'Date_of_Journey']:
    change_into_datetime(feature)
# after converting the data types we look into it again it make sure it has done 
print(data.dtypes)
# converting the date of jounery column to day,month and year for better analysis
data['Journey_day'] = data['Date_of_Journey'].dt.day
data['Journey_month'] = data['Date_of_Journey'].dt.month
data['Journey_year'] = data['Date_of_Journey'].dt.year
# Reading the data
print(data.head(2))