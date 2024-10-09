import pandas as pd
import simplekml

df = pd.read_csv('Dataset .csv')

kml = simplekml.Kml()

for _, row in df.iterrows():
    kml.newpoint(
        name=row['Restaurant Name'],
        coords=[(row['Longitude'], row['Latitude'])]
    )

kml.save('restaurants.kml')
print("KML file has been saved as 'restaurants.kml' open this file in google earth")
