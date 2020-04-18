#Random Forest Regression


#Importing the Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Importing the Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


#Regressor
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=1000,random_state=0)
regressor.fit(X,y)


#Predicting a new result with Linear Regression
regressor.predict([[6.5]])



#Visualising the  Regression Model 
X_grid = np.arange(min(X),max(X),0.01) #This gives us a vector
X_grid = X_grid.reshape((len(X_grid),1)) # To convert it back to matrix
plt.scatter(X,y,color = 'Red')
plt.plot(X_grid,regressor.predict(X_grid),color = 'blue')
plt.title('Truth or Bluff(Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show