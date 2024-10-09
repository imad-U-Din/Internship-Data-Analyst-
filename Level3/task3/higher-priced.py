import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset .csv')  

df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})

online_delivery_palette = {0: 'darkblue', 1: 'skyblue'}
table_booking_palette = {0: 'green', 1: 'lightgreen'}

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Price range', hue='Has Online delivery', palette=online_delivery_palette)
plt.title('Count of Online Delivery Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.legend(title='Online Delivery', labels=['No', 'Yes'])
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Price range', hue='Has Table booking', palette=table_booking_palette)
plt.title('Count of Table Booking Availability by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Count')
plt.legend(title='Table Booking', labels=['No', 'Yes'])
plt.show()

proportion_delivery = df.groupby('Price range')['Has Online delivery'].mean()
proportion_booking = df.groupby('Price range')['Has Table booking'].mean()

print("Proportion of online delivery by price range:")
print(proportion_delivery)

print("Proportion of table booking by price range:")
print(proportion_booking)

plt.figure(figsize=(12, 6))
proportion_delivery.plot(kind='bar', color='purple')
plt.title('Proportion of Online Delivery by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion')
plt.show()

plt.figure(figsize=(12, 6))
proportion_booking.plot(kind='bar', color='yellow')
plt.title('Proportion of Table Booking by Price Range')
plt.xlabel('Price Range')
plt.ylabel('Proportion')
plt.show()
