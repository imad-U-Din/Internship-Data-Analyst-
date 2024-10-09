import pandas as pd
from sklearn.cluster import KMeans
import simplekml

df = pd.read_csv('Dataset .csv')

X = df[['Latitude', 'Longitude']].values

kmeans = KMeans(n_clusters=5, random_state=0).fit(X)  
df['Cluster'] = kmeans.labels_

kml = simplekml.Kml()

styles = {
    cluster: simplekml.Style(
        iconstyle=simplekml.IconStyle(icon='http://maps.google.com/mapfiles/kml/paddle/red-circle.png')
    )
    for cluster in df['Cluster'].unique()
}

for idx, row in df.iterrows():
    placemark = kml.newpoint(
        name=row['Restaurant Name'],
        coords=[(row['Longitude'], row['Latitude'])],
        description=f"Cluster {row['Cluster']}"
    )
    placemark.style = styles[row['Cluster']]

kml.save('restaurants_clusters.kml')
print("KML file has been saved as 'restaurants_clusters.kml' open this file in google earth")
