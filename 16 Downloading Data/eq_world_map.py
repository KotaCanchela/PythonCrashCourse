import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = "16 Downloading Data/eq_data_30_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# Making the data more readable
readable_file = "16 Downloading Data/mapping_global_data/readable_eq_data.json"
with open(readable_file, "w") as f:
    json.dump(all_eq_data, f, indent=4)

# Obtaining the total amount of earthquakes occurred in the data
all_eq_dicts = all_eq_data["features"]  # Dictionary now stored in a list
print(len(all_eq_dicts))

# Pull the magnitude, longitude, and latitude of each earthquake
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    hover_texts.append(eq_dict["properties"]["title"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
print(mags[:10])
print(lons[:10])
print(lats[:10])

# Map the earthquakes


data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        'text': hover_texts,
        "marker": {
            "size": [3 * mag for mag in mags],
            "color": mags,
            "colorscale": "Hot",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title=f"{all_eq_data['metadata']['title']}")


fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")

