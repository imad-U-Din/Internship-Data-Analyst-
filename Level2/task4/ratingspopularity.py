import pandas as pd

data = pd.read_csv("Dataset .csv")  
df = pd.DataFrame(data)

required_columns = ['Restaurant Name', 'Aggregate rating', 'Votes']
for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")

restaurant_counts = df['Restaurant Name'].value_counts()

restaurant_chains_df = restaurant_counts.reset_index()
restaurant_chains_df.columns = ['Restaurant Name', 'Count']

df_chains = df[df['Restaurant Name'].isin(restaurant_chains_df['Restaurant Name'])]

restaurant_analysis = df_chains.groupby('Restaurant Name').agg({
    'Aggregate rating': 'mean',  
    'Votes': 'sum',  
    'Restaurant Name': 'count'  
}).rename(columns={'Restaurant Name': 'Count'})

restaurant_analysis = restaurant_analysis.reset_index()

restaurant_analysis_sorted = restaurant_analysis.sort_values(by='Count', ascending=False)

print("Analysis of Restaurant Chains:")
print(restaurant_analysis_sorted.to_string(index=False))


