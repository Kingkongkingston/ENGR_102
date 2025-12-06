# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Kingston Alexander
# Section:      509
# Assignment:   Topic 12 Individual Lab: Plotting Data
# Date:         25 Nov 2025

import matplotlib.pyplot as plt
import csv
from collections import defaultdict


def read_weather():
    dates = []
    avg_wet_bulb = []
    avg_pressure = []
    avg_wind = []
    avg_rh = []
    avg_dew = []
    avg_temp = []
    high_temp = []
    low_temp = []
    precip = []

    with open("WeatherDataCLL.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            dates.append(row["Date"])

            def safe_float(x):
                return float(x) if x.strip() != "" else 0.0

            avg_dew.append(safe_float(row["Average Dew Point (F)"]))
            avg_pressure.append(safe_float(row["Average Pressure (in Hg)"]))
            avg_wet_bulb.append(safe_float(
                row["Average Wet Bulb Temperature (F)"]))
            avg_wind.append(safe_float(row["Average Daily Wind Speed (mph)"]))
            precip.append(safe_float(row["Precipitation (in)"]))
            avg_rh.append(safe_float(row["Average Relative Humidity (%)"]))
            avg_temp.append(safe_float(row["Average Temperature (F)"]))
            high_temp.append(safe_float(row["Maximum Temperature (F)"]))
            low_temp.append(safe_float(row["Minimum Temperature (F)"]))

    return (dates, avg_wet_bulb, avg_pressure, avg_wind,
            avg_rh, avg_dew, avg_temp, high_temp, low_temp, precip)


def main():
    (dates, avg_wet_bulb, avg_pressure, avg_wind, avg_rh, avg_dew,
     avg_temp, high_temp, low_temp, precip) = read_weather()

    # Line graph
    plt.figure()
    plt.plot(avg_wet_bulb, label="Avg Wet Bulb")
    plt.xlabel("Day Index")
    plt.ylabel("Avg Wet Bulb")

    # second y-axis
    ax2 = plt.twinx()
    ax2.plot(avg_pressure, color="orange", label="Avg Pressure")
    ax2.set_ylabel("Avg Pressure")

    plt.title("Avg Wet Bulb and Avg Pressure Over Time")
    plt.legend()
    plt.show()

    # Histogram of wind speed
    plt.figure()
    plt.hist(avg_wind, bins=15)
    plt.xlabel("Average Wind Speed")
    plt.ylabel("Number of Days")
    plt.title("Histogram of Average Wind Speed")
    plt.show()

    # Scatterplot RH vs Dew Point
    plt.figure()
    plt.scatter(avg_rh, avg_dew)
    plt.xlabel("Average Relative Humidity")
    plt.ylabel("Average Dew Point")
    plt.title("RH vs Dew Point Scatterplot")
    plt.show()

    # Monthly statistics bar chart

    monthly_temp = defaultdict(list)
    monthly_high = defaultdict(list)
    monthly_low = defaultdict(list)
    monthly_precip = defaultdict(list)

    for i, d in enumerate(dates):
        month = int(d.split("/")[0])
        monthly_temp[month].append(avg_temp[i])
        monthly_high[month].append(high_temp[i])
        monthly_low[month].append(low_temp[i])
        monthly_precip[month].append(precip[i])

    months = list(range(1, 13))
    mean_temp = [sum(monthly_temp[m]) / len(monthly_temp[m]) for m in months]
    max_high = [max(monthly_high[m]) for m in months]
    min_low = [min(monthly_low[m]) for m in months]
    mean_precip = [sum(monthly_precip[m]) / len(monthly_precip[m])
                   for m in months]

    plt.figure()
    plt.bar(months, mean_temp, label="Mean Avg Temp")
    plt.plot(months, max_high, label="Highest High Temp")
    plt.plot(months, min_low, label="Lowest Low Temp")
    plt.plot(months, mean_precip, label="Mean Total Precip")

    plt.xlabel("Month")
    plt.ylabel("Temperature / Precip")
    plt.title("Monthly Temperature and Precipitation Stats")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
