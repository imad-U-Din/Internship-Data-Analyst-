import pandas as pd

df = pd.read_csv('Dataset .csv')

print(df.head())

df['Has Online delivery'] = df['Has Online delivery'].apply(lambda x: x.strip().lower() == 'yes')

total_restaurants = len(df)

num_with_delivery = df['Has Online delivery'].sum()

percentage_with_delivery = (num_with_delivery / total_restaurants) * 100

print(f"Percentage of restaurants offering online delivery: {percentage_with_delivery:.2f}%")
