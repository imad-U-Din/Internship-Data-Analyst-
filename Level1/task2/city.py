import pandas as pd


df = pd.read_csv('Dataset .csv')

city_avg_ratings = df.groupby('City')['Aggregate rating'].mean()

highest_avg_rating_city = city_avg_ratings.idxmax()
highest_avg_rating_value = city_avg_ratings.max()

print(f"\nThe city with the highest average rating is '{highest_avg_rating_city}'")
print(f"With an average rating of {highest_avg_rating_value:.2f}")
