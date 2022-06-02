# Loading modules
import pandas as pd
import pycountry as pc
import geopandas as gpd
import folium

# Loading data (txt) in variable
with open('data/affiliation-E2.txt') as f:
    affiliation = f.read()

# Read the geopandas countries dataset list
world_countries_list = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Extracting the name country from the affiliation data
for c in pc.countries:
    if c.name in affiliation:
        # check if the country is in the list
        if c.name in world_countries_list['name'].tolist():
            # Get the index of the country in the list
            index = world_countries_list.index[world_countries_list['name'] == c.name].tolist()[0]
            # Add the number of papers in the country
            world_countries_list.loc[index, 'papers'] = affiliation.count(c.name)
        
# Cleaning the dataframe nan values
world_countries_list = world_countries_list.dropna()

# Create a map
my_map = folium.Map(tiles="cartodbpositron")
# Add the data
folium.Choropleth(
    geo_data=world_countries_list,
    name='choropleth',
    data=world_countries_list,
    columns=['name', 'papers'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Papers Published in LAC'
).add_to(my_map)

# Save the map
my_map.save('papers_lac.html')