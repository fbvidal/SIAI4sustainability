# Loading modules
from itertools import count
import pandas as pd
import pycountry
import geopandas as gpd
import folium


# Loading data from CSV file to Pandas DataFrame (see data folder for more information)
scopus_data = pd.read_csv('data/Scopus/E3-scopus.csv')

# Selecting colunms from DataFrame Affiliations and convert to string
affiliation = str(scopus_data['Affiliations'].tolist())

# Read the geopandas countries dataset list
world_countries_list = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Counting numbers of papers in each country in the list
results = []
for country in pycountry.countries:
    results.append({
            "count": affiliation.count(country.name),
            "key": country.alpha_3,
            "country": "{}".format(country.name),})

# Convert list to dataframe
results_df = pd.DataFrame(results)


# merging the dataframe with the geopandas dataset
world_countries_list = world_countries_list.merge(results_df, left_on='iso_a3', right_on='key')

#cleaning the dataframe nan values
world_countries_list = world_countries_list.dropna()
#cleaning rows with 0 papers
world_countries_list = world_countries_list[world_countries_list['count'] != 0]

print(world_countries_list)

# Create a map
my_map = folium.Map(tiles="cartodbpositron")
# Add the data
folium.Choropleth(
    geo_data=world_countries_list,
    name='choropleth',
    data=world_countries_list,
    columns=['name', 'count'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Papers Published Scopus Expression E3'
).add_to(my_map)

# Save the map
my_map.save('out/Scopus/papers_scopus_E3.html')