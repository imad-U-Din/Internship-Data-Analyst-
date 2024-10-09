import pandas as pd

df = pd.read_csv('Dataset .csv')  

print("Dataset preview:")
print(df.head())

df['Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

sorted_df = df.sort_values(by='Votes', ascending=False)

sorted_df = sorted_df[['Restaurant Name', 'Votes']]

print("\nRestaurants with the Highest Number of Votes:")
print(sorted_df.head(15))

print("\nRestaurants with the Lowest Number of Votes:")
print(sorted_df.tail(15))
