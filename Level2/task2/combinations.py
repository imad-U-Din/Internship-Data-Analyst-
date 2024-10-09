import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Dataset .csv")

cuisine_counts = data["Cuisines"].value_counts()

top_cuisines = cuisine_counts.head(25)

print(top_cuisines)

top_cuisines.plot(kind="bar")
plt.title("Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Frequency")
plt.show()