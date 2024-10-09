import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

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

anova_delivery = f_oneway(
    *[df[df['Price range'] == pr]['Has Online delivery'] for pr in df['Price range'].unique()]
)
print(f"ANOVA result for online delivery:\nF-statistic: {anova_delivery.statistic}\nP-value: {anova_delivery.pvalue}")

anova_booking = f_oneway(
    *[df[df['Price range'] == pr]['Has Table booking'] for pr in df['Price range'].unique()]
)
print(f"ANOVA result for table booking:\nF-statistic: {anova_booking.statistic}\nP-value: {anova_booking.pvalue}")
