import pandas as pd


df = pd.read_csv('Dataset .csv')


city_avg_ratings = df.groupby('City')['Aggregate rating'].mean().reset_index()


city_avg_ratings.columns = ['City', 'Aggregate rating']


print(city_avg_ratings)
