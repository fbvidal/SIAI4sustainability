# Loading modules
import pandas as pd
import geopandas as gpd
import folium

# Loading data (csv) in a Dataframe
countries = pd.read_csv('data/countries.csv')

# Read the geopandas dataset
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Merge the dataframe with the geopandas dataset
merged_countries = world.merge(countries, how="left", left_on=['name'], right_on=['Country'])

# Cleaning the dataframe nan values
merged_countries = merged_countries.dropna()

# Create a map
my_map = folium.Map(tiles="cartodbpositron")
# Add the data
folium.Choropleth(
    geo_data=merged_countries,
    name='choropleth',
    data=merged_countries,
    columns=['Country', 'papers'],
    key_on='feature.properties.name',
    fill_color='OrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Papers Published'
).add_to(my_map)

my_map.save('papers_all.html')