import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset .csv') 

print("Dataset preview:")
print(df.head())

df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

df = df.dropna(subset=['Votes', 'Aggregate rating'])

correlation = df[['Votes', 'Aggregate rating']].corr().iloc[0, 1]
print(f"\nCorrelation between Votes and Aggregate rating: {correlation:.2f}")

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Votes', y='Aggregate rating', alpha=0.7)
plt.title('Scatter Plot of Votes vs Aggregate rating')
plt.xlabel('Number of Votes')
plt.ylabel('Aggregate rating')
plt.grid(True)
plt.show()
