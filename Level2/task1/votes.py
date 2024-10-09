import pandas as pd

df = pd.read_csv('Dataset .csv')

print(df.head())
print(df.columns)

votes_column = 'Votes'  

df[votes_column] = pd.to_numeric(df[votes_column], errors='coerce')
df = df.dropna(subset=[votes_column])

average_votes = df[votes_column].mean()

print(f"Average Number of Votes Received by Restaurants: {average_votes:.2f}")
