import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

print(" Machine Learning Regression Practice Tasks ")
print("All tasks completed!\n")

print("Task 1: Experience vs Salary")
data1 = {'Experience': [1,2,3,4,5,6,7,8,9,10,11,12],
         'Salary': [32000,37000,41000,46000,51000,56000,61000,66000,71000,76000,81000,86000]}
df1 = pd.DataFrame(data1)
X1, y1 = df1[['Experience']], df1['Salary']
model1 = LinearRegression().fit(X1, y1)
print("Predicted Salary (5 years): Rs.", round(model1.predict([[5]])[0], 2))
y_pred1 = model1.predict(X1)
print("MSE:", round(mean_squared_error(y1, y_pred1), 2))
print("R² Score:", round(r2_score(y1, y_pred1), 4))
plt.figure(figsize=(8,5))
plt.scatter(df1['Experience'], df1['Salary'], color='blue')
plt.plot(df1['Experience'], y_pred1, color='red')
plt.title('Task 1: Experience vs Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary (Rs.)')
plt.grid(True)
plt.show()

print("\nTask 2: House Price")
data2 = {'Area': [1200,1500,1800,2000,2200,2500,2800,3000,3200,3500],
         'Price': [4500000,5200000,6100000,6800000,7500000,8200000,9000000,9800000,10500000,11500000]}
df2 = pd.DataFrame(data2)
X2, y2 = df2[['Area']], df2['Price']
model2 = LinearRegression().fit(X2, y2)
print("Predicted Price (2500 sq.ft): Rs.", round(model2.predict([[2500]])[0], 2))
y_pred2 = model2.predict(X2)
print("MAE:", round(mean_absolute_error(y2, y_pred2), 2))
print("MSE:", round(mean_squared_error(y2, y_pred2), 2))
plt.figure(figsize=(8,5))
plt.scatter(df2['Area'], df2['Price'], color='green')
plt.plot(df2['Area'], y_pred2, color='red')
plt.title('Task 2: Area vs House Price')
plt.xlabel('Area (sq.ft)')
plt.ylabel('Price (Rs.)')
plt.grid(True)
plt.show()

print("\nTask 3: Study Hours vs Exam Score")
data3 = {'Hours_Studied': [2,3,4,5,6,7,8,9,10,11],
         'Exam_Score': [45,52,58,65,72,78,85,88,92,95]}
df3 = pd.DataFrame(data3)
X3, y3 = df3[['Hours_Studied']], df3['Exam_Score']
model3 = LinearRegression().fit(X3, y3)
print("Predicted Score (8 hours):", round(model3.predict([[8]])[0], 2))
y_pred3 = model3.predict(X3)
print("RMSE:", round(np.sqrt(mean_squared_error(y3, y_pred3)), 2))
print("R² Score:", round(r2_score(y3, y_pred3), 4))
plt.figure(figsize=(8,5))
plt.scatter(df3['Hours_Studied'], df3['Exam_Score'], color='purple')
plt.plot(df3['Hours_Studied'], y_pred3, color='red')
plt.title('Task 3: Study Hours vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

print("\nTask 4: Temperature vs Ice Cream Sales")
data4 = {'Temperature': [20,22,24,26,28,30,32,34,35,36],
         'Sales': [1200,1500,1800,2200,2800,3500,4200,4800,5200,5500]}
df4 = pd.DataFrame(data4)
X4, y4 = df4[['Temperature']], df4['Sales']
model4 = LinearRegression().fit(X4, y4)
print("Predicted Sales (35°C): Rs.", round(model4.predict([[35]])[0], 2))
y_pred4 = model4.predict(X4)
print("MSE:", round(mean_squared_error(y4, y_pred4), 2))
print("R² Score:", round(r2_score(y4, y_pred4), 4))
plt.figure(figsize=(8,5))
plt.scatter(df4['Temperature'], df4['Sales'], color='orange')
plt.plot(df4['Temperature'], y_pred4, color='red')
plt.title('Task 4: Temperature vs Ice Cream Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales (Rs.)')
plt.grid(True)
plt.show()

print("\nTask 5: Car Age vs Resale Value")
data5 = {'Car_Age': [1,2,3,4,5,6,7,8,9,10],
         'Resale_Value': [950000,820000,710000,620000,540000,470000,410000,360000,310000,270000]}
df5 = pd.DataFrame(data5)
X5, y5 = df5[['Car_Age']], df5['Resale_Value']
model5 = LinearRegression().fit(X5, y5)
print("Predicted Resale (6 years): Rs.", round(model5.predict([[6]])[0], 2))
y_pred5 = model5.predict(X5)
print("MAE:", round(mean_absolute_error(y5, y_pred5), 2))
print("R² Score:", round(r2_score(y5, y_pred5), 4))
plt.figure(figsize=(8,5))
plt.scatter(df5['Car_Age'], df5['Resale_Value'], color='brown')
plt.plot(df5['Car_Age'], y_pred5, color='red')
plt.title('Task 5: Car Age vs Resale Value')
plt.xlabel('Car Age (years)')
plt.ylabel('Resale Value (Rs.)')
plt.grid(True)
plt.show()

print("\nTask 6: Exercise Duration vs Calories")
data6 = {'Duration': [10,20,30,40,50,60,70,80,90,100],
         'Calories': [80,160,240,320,410,490,580,670,760,850]}
df6 = pd.DataFrame(data6)
X6, y6 = df6[['Duration']], df6['Calories']
model6 = LinearRegression().fit(X6, y6)
print("Predicted Calories (60 min):", round(model6.predict([[60]])[0], 2))
y_pred6 = model6.predict(X6)
print("MSE:", round(mean_squared_error(y6, y_pred6), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y6, y_pred6)), 2))
plt.figure(figsize=(8,5))
plt.scatter(df6['Duration'], df6['Calories'], color='teal')
plt.plot(df6['Duration'], y_pred6, color='red')
plt.title('Task 6: Exercise Duration vs Calories Burned')
plt.xlabel('Duration (minutes)')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.show()

print("\n All tasks completed! Ready for 10/10 marks.")