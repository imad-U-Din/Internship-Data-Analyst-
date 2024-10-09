import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Dataset .csv')

print(df.head())
print(df.info())

grouped_df = df.groupby('Cuisines')['Aggregate rating'].mean().reset_index()

grouped_df.columns = ['Cuisine', 'Average Rating']

top_25_avg_rating = grouped_df.nlargest(25, 'Average Rating')

print(top_25_avg_rating)

plt.figure(figsize=(12, 6))
sns.barplot(x='Cuisine', y='Average Rating', data=top_25_avg_rating)
plt.xticks(rotation=90)
plt.title('Top 25 Cuisines by Average Rating')
plt.xlabel('Cuisine')
plt.ylabel('Average Rating')
plt.show()
