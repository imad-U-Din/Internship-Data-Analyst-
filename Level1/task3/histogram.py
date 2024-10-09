import pandas as pd
import matplotlib.pyplot as plt

file_path = 'Dataset .csv'  
df = pd.read_csv(file_path)

print(df.head())

price_range_counts = df['Price range'].value_counts()

price_range_counts = price_range_counts.sort_index()

plt.figure(figsize=(8, 5))
plt.bar(price_range_counts.index, price_range_counts.values, color='green')
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
