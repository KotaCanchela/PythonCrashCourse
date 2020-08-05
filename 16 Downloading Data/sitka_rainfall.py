import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.pyplot import figure

filename = "/Users/Kota/Desktop/pcc_2e-master/chapter_16/the_csv_file_format/data/sitka_weather_07-2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Get index number and value of each item in the header_row list
    for index, column_header in enumerate(header_row):
        print(index, column_header)
    # Get dates and high temperatures from this file.
    dates, rainfall = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}.")
        else:
            dates.append(current_date)
            rainfall.append(rain)
print(
    f"---------------Rainfall---------------\n{rainfall}"
)

# Plot the high temperatures
plt.style.use("seaborn")
fig, ax = plt.subplots(figsize=(14, 8))
ax.plot(dates, rainfall, c="red", alpha=0.5)
# Format the plot
title = "Daily rainfall - 2018\Sitka, Alaska"
plt.title(title, fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()

