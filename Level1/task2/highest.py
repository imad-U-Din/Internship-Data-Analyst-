import pandas as pd


df = pd.read_csv('Dataset .csv')

city_counts = df['City'].value_counts()


city_with_most_restaurants = city_counts.idxmax()
number_of_restaurants = city_counts.max()

print(f"\nThe city with the highest average rating is '{city_with_most_restaurants}'")
print(f"With an average rating of {number_of_restaurants:.2f}")




