import pandas as pd

df = pd.read_csv('Dataset .csv')


Cuisines_counts = df['Cuisines'].value_counts()


top_three_Cuisines = Cuisines_counts.head(3)


print("Top Three Most Common Cuisines:")
print(top_three_Cuisines)
