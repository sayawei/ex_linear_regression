import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

np.random.seed(42)
area = 2.5 * np.random.randn(100) + 25
price = 5 * area + np.random.randn(100) * 10 + 100

houses = pd.DataFrame({
    'Area': area,
    'Price': price
})

X = houses[['Area']].values
y = houses['Price'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred)}")
print(f"R-squared Score: {r2_score(y_test, y_pred)}")

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Prices')
plt.scatter(X_test, y_pred, color='red', label='Predicted Prices')
plt.plot(X_test, y_pred, color='green', linewidth=2, label='Regression Line') 
plt.xlabel("Area (square meters)")
plt.ylabel("Price ($)")
plt.title("Linear Regression: Price vs Area")
plt.legend()
plt.show()
