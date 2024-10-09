import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('Dataset .csv')  

print("First few rows of the dataset:")
print(df.head())

df['review_length'] = df['Rating text'].apply(len)

average_length = df['review_length'].mean()
print(f'\nAverage review length: {average_length:.2f} characters')

average_rating = df['Aggregate rating'].mean()
print(f'Average rating: {average_rating:.2f}')

correlation = df[['review_length', 'Aggregate rating']].corr().iloc[0, 1]
print(f'\nCorrelation between review length and rating: {correlation:.2f}')

plt.figure(figsize=(10, 6))
plt.scatter(df['review_length'], df['Aggregate rating'], alpha=0.5, color='blue')
plt.title('Review Length vs. Rating')
plt.xlabel('Review Length (characters)')
plt.ylabel('Rating')
plt.grid(True)
plt.show()

X = df[['review_length']].values.reshape(-1, 1)  
y = df['Aggregate rating'].values  

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

plt.figure(figsize=(10, 6))
plt.scatter(df['review_length'], df['Aggregate rating'], alpha=0.5, color='blue', label='Data points')
plt.plot(df['review_length'], y_pred, color='red', linewidth=2, label='Regression line')
plt.title('Review Length vs. Rating with Regression Line')
plt.xlabel('Review Length (characters)')
plt.ylabel('Rating')
plt.legend()
plt.grid(True)
plt.show()
