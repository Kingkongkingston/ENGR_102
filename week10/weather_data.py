# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   11.17 Lab: Weather Data
# Date:         18 Nov 2025

# weather_data.py

import csv
from statistics import mean
import calendar

# Read the CSV file
filename = "WeatherDataCLL.csv"

data = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)  # default delimiter is comma
    for row in reader:
        # Convert numeric fields, skip missing values
        for key in row:
            if key != "Date":
                try:
                    row[key] = float(row[key])
                except ValueError:
                    row[key] = None
        data.append(row)

# Compute 10-year max and min temperatures
max_temp = max(row["Maximum Temperature (F)"]
               for row in data if row["Maximum Temperature (F)"] is not None)
min_temp = min(row["Minimum Temperature (F)"]
               for row in data if row["Minimum Temperature (F)"] is not None)

print(f"10-year maximum temperature: {int(max_temp)} F")
print(f"10-year minimum temperature: {int(min_temp)} F\n")

# Ask user for month and year
month_input = input("Please enter a month: ").strip()
year_input = input("Please enter a year: ").strip()

# Filter data for requested month and year
filtered = []
for row in data:
    date_parts = row["Date"].split("/")
    row_month = int(date_parts[0])
    row_year = date_parts[2]
    if row_year == year_input and calendar.month_name[row_month].lower() == month_input.lower():
        filtered.append(row)

if not filtered:
    print(f"No data found for {month_input} {year_input}.")
    exit()

# Helper function to calculate mean ignoring None


def mean_ignore_none(values):
    valid = [v for v in values if v is not None]
    return mean(valid) if valid else None


# Calculate statistics
mean_pressure = mean_ignore_none(
    [row["Average Pressure (in Hg)"] for row in filtered])
mean_temp = mean_ignore_none(
    [row["Average Temperature (F)"] for row in filtered])
mean_wet_bulb = mean_ignore_none(
    [row["Average Wet Bulb Temperature (F)"] for row in filtered])
mean_dew_point = mean_ignore_none(
    [row["Average Dew Point (F)"] for row in filtered])
mean_humidity = mean_ignore_none(
    [row["Average Relative Humidity (%)"] for row in filtered])
mean_wind = mean_ignore_none(
    [row["Average Daily Wind Speed (mph)"] for row in filtered])
precip_days = sum(
    1 for row in filtered if row["Precipitation (in)"] and row["Precipitation (in)"] > 0)
precip_percent = (precip_days / len(filtered)) * 100

# Print results
print(f"\nFor {month_input} {year_input}:")
print(f"Mean average daily pressure: {mean_pressure:.2f} in Hg")
print(f"Mean average daily temperature: {mean_temp:.1f} F")
print(f"Mean average daily wet bulb temperature: {mean_wet_bulb:.1f} F")
print(f"Mean average daily dew point: {mean_dew_point:.1f} F")
print(f"Mean average daily relative humidity: {mean_humidity:.1f}%")
print(f"Mean average daily wind speed: {mean_wind:.2f} mph")
print(f"Percentage of days with precipitation: {precip_percent:.1f}%")
