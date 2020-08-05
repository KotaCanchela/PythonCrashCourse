import json

# Explore the structure of the data.
filename = "/Users/Kota/Desktop/pcc_2e-master/chapter_16/mapping_global_data_sets/data/eq_data_1_day_m1.json"
with open(filename) as f:
    all_eq_data = json.load(f)

# Making the data more readable
readable_file = '16 Downloading Data/mapping_global_data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Obtaining the total amount of earthquakes occurred in the data
all_eq_dicts = all_eq_data['features']  # Dictionary now stored in a list
print(len(all_eq_dicts))

# Pull the magnitude, longitude, and latitude of each earthquake
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:10])
print(lats[:10])
