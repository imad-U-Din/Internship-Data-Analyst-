import pandas as pd


df = pd.read_csv('Dataset .csv')


total_restaurants = len(df)


cuisine_counts = df['Cuisines'].value_counts()


cuisine_percentages = (cuisine_counts / total_restaurants) * 100


print("Percentage of restaurants serving each cuisine:")
print(cuisine_percentages)

