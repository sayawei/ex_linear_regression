import pandas as pd

houses = pd.read_csv(r"C:/Users/User/Desktop/House_Price_Prediction_Dataset.csv")

X = houses.iloc[:, :-1].values
Y = houses.iloc[:, 4].values

print(houses.head())