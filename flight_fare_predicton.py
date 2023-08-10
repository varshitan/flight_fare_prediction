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

# Creating a copy of this data so manipulations can be done on the other dataset
data = train_data.copy()

# Changing the datatype to datetime since the machine cannot understand the object type 
# Instead of writing long codes, we define a function because whenever there is a repetition of data, it's better to define a function
def change_into_datetime(col):
    data[col] = pd.to_datetime(data[col], dayfirst=True)

# Giving all the features that need to be converted in a list and then calling the change_into_datetime function
for feature in ['Dep_Time', 'Arrival_Time', 'Date_of_Journey']:
    change_into_datetime(feature)

# After converting the data types, we look into it again to make sure it has been done
print(data.dtypes)

# Converting the date of journey column to day, month, and year for better analysis
data['Journey_day'] = data['Date_of_Journey'].dt.day
data['Journey_month'] = data['Date_of_Journey'].dt.month
data['Journey_year'] = data['Date_of_Journey'].dt.year

# Reading the data
print(data.head(2))

# Now converting the time feature to hours and minutes
def extract_hour_min(df, col):
    df[col + '_hour'] = df[col].dt.hour
    df[col + '_minute'] = df[col].dt.minute
    return df

print(extract_hour_min(data, 'Dep_Time'))
print(extract_hour_min(data, 'Arrival_Time'))

# After extracting these features, we can drop the previous columns since they all contain the same info but in different columns and types
cols_to_drop = ['Arrival_Time', 'Dep_Time']
data.drop(cols_to_drop, axis=1, inplace=True)

# Now we will start analyzing the data

# Let's analyze in which time most of the flights take off
def flight_dep_time(x):
    if (x <= 4) and (x <= 8):
        return 'Early morning'
    elif (x > 8) and (x <= 12):
        return 'Morning'
    elif (x > 12) and (x <= 16):
        return 'Noon'
    elif (x > 16) and (x <= 20):
        return 'Evening'
    elif (x > 20) and (x <= 2):
        return 'Night'
    else:
        return 'Late night'

# To know the number of flights we use the value count method to it
data['Dep_Time_Hour_category'] = data['Dep_Time_hour'].apply(flight_dep_time)
flight_counts = data['Dep_Time_Hour_category'].value_counts()

print(flight_counts)
# plotting the flght counts for better understanding of data


# To make graphs itnteractive we use plotly

plt.bar(flight_counts.index, flight_counts, color='blue')
plt.xlabel('Departure Time Category')
plt.ylabel('Number of Flights')
plt.title('Number of Flights by Departure Time Category')
plt.xticks(rotation=45)
plt.show()

def pre_Process_duration (x):
    if 'h'not in x:
        x= '0h'+ '' +x
    elif 'm' not in x:
        x  = x + ''+'0m'
    return x

data['Duration']= data['Duration'].apply(pre_Process_duration)
print(data['Duration'])
data['Duration_hours']= data['Duration'].apply(lambda x :int(x.split('')[0][0:-1]))
data['Duration_mins']= data['Duration'].apply(lambda x :int(x.split('')[1][0:-1]))
    


