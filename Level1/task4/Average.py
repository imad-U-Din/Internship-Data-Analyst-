import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset .csv')  

df = df.dropna(subset=['Aggregate rating', 'Has Online delivery'])

average_ratings = df.groupby('Has Online delivery')['Aggregate rating'].mean().reset_index()

average_ratings.columns = ['Has Online Delivery', 'Average Rating']

print("Average Ratings by Online Delivery Status:")
print(average_ratings)

plt.figure(figsize=(10, 6))
sns.barplot(x='Has Online Delivery', y='Average Rating', data=average_ratings, palette='viridis')
plt.xlabel('Has Online Delivery')
plt.ylabel('Average Rating')
plt.title('Comparison of Average Ratings for Restaurants With and Without Online Delivery')
plt.xticks(ticks=[0, 1], labels=['No', 'Yes'])
plt.ylim(0, average_ratings['Average Rating'].max() + 1)  
plt.show()
