# Multiple Linear Regression

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')

#Checking Nulls
nulls = pd.DataFrame(dataset.isnull().sum().sort_values(ascending=False)[:5])
nulls.columns  = ['Null Count']
nulls.index.name  = 'Feature'
print(nulls)

#Correlation
numeric_features  = dataset.select_dtypes(include=[np.number])
corr = numeric_features.corr()
print("Correlation\n",corr['Profit'].sort_values(ascending=False)[1:4],'\n')

#Splitting Independant and Dependant 
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Checking Skew
print("Skew\n",dataset.Profit.skew())
plt.hist(dataset.Profit)
plt.show()

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

##Evaluate the performance 
print ("R^2 is: \n", regressor.score(X_test, y_test))

from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, y_pred))