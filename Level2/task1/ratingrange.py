import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset .csv')  

print(df.head())
print(df.info())
print(df.describe())

df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

df = df.dropna(subset=['Aggregate rating'])

plt.figure(figsize=(10, 6))
plt.hist(df['Aggregate rating'], bins=range(int(df['Aggregate rating'].min()), int(df['Aggregate rating'].max()) + 1), edgecolor='black')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

rating_bins = [0, 1, 2, 3, 4, 5] 
rating_labels = ['0-1', '1-2', '2-3', '3-4', '4-5']  

df['rating_range'] = pd.cut(df['Aggregate rating'], bins=rating_bins, labels=rating_labels, right=False)

rating_range_counts = df['rating_range'].value_counts().sort_index()

most_common_range = rating_range_counts.idxmax()
most_common_count = rating_range_counts.max()
print(f"Most Common Rating Range: {most_common_range} with {most_common_count} occurrences")

plt.figure(figsize=(10, 6))
rating_range_counts.plot(kind='bar', color='cyan', edgecolor='black')
plt.title('Frequency of Rating Ranges')
plt.xlabel('Rating Range')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
