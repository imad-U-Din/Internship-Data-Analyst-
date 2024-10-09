import pandas as pd

data = pd.read_csv("Dataset .csv")  
df = pd.DataFrame(data)

restaurant_counts = df['Restaurant Name'].value_counts()

restaurant_chains_df = restaurant_counts.reset_index()
restaurant_chains_df.columns = ['Restaurant Name', 'Count']

print("Restaurant chains present in the dataset:")
print(restaurant_chains_df.to_string(index=False))
