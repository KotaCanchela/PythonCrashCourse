import csv
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.patches as mpatches


filename = "16 Downloading Data/2229225.csv"  # Data containing dates, location, and precipitation amount by city (Lake Stevens and San Francisco)
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get index number and value of each item in the header_row list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Get dates and high temperatures from this file.
    dates_ls, dates_sf, names, precip_ls, precip_sf = [], [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[5], "%Y-%m-%d")
        try:
            name = row[1]
            prcp = float(row[6])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            if "LAKE STEVENS 3.2 N, WA US" in name:
                precip_ls.append(prcp)
                dates_ls.append(current_date)
                names.append(name)

            elif "SAN FRANCISCO DOWNTOWN, CA US" in name:
                precip_sf.append(prcp)
                dates_sf.append(current_date)
                names.append(name)

# Plot the high temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(dates_ls, precip_ls, c="red", alpha=0.5)
ax.plot(dates_sf, precip_sf, c="blue", alpha=0.5)
red_patch = mpatches.Patch(color="red", label="Lake Stevens")
blue_patch = mpatches.Patch(color="blue", label="San Francisco")

plt.legend(handles=[red_patch, blue_patch])


# Format the plot
title = "Daily Precipitation\nLake Stevens, WA & San Francisco, CA"
plt.title(title, fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
