import pandas as pd

df = pd.read_csv('Dataset .csv')
price_range_counts = df['Price range'].value_counts()

total_restaurants = len(df)
price_range_percentages = (price_range_counts / total_restaurants) * 100

formatted_df = price_range_percentages.reset_index()
formatted_df.columns = ['Price Range', 'Percentage']

formatted_df.sort_values(by='Percentage', ascending=False, inplace=True)

formatted_df.reset_index(drop=True, inplace=True)

print("\nPercentage of Restaurants in Each Price Range Category:\n")
print(f"{'Price Range':<15} {'Percentage':>10}")
print('-' * 25)
for index, row in formatted_df.iterrows():
    print(f"{row['Price Range']:<15} {row['Percentage']:>9.2f}%")
