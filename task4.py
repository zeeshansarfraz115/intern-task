import pandas as pd

# Creating the dataset because i didn't had dataset given in class.

data = {
    "City": [
        "Karachi",
        "Lahore",
        "Faisalabad",
        "Rawalpindi",
        "Peshawar",
        "Multan",
        "Hyderabad",
        "Islamabad",
        "Quetta",
        "Sialkot"
    ],

    "Province": [
        "Sindh",
        "Punjab",
        "Punjab",
        "Punjab",
        "Khyber Pakhtunkhwa",
        "Punjab",
        "Sindh",
        "Federal Capital Territory",
        "Balochistan",
        "Punjab"
    ],

    "Population_2024": [
        18800000,
        13350000,
        3280000,
        2360000,
        2060000,
        1950000,
        1840000,
        1240000,
        1130000,
        925000
    ],

    "Growth_Rate": [
        1.62,
        2.69,
        2.50,
        2.61,
        3.00,
        2.63,
        2.22,
        3.33,
        2.73,
        2.78
    ]
}

df = pd.DataFrame(data)

print("Complete Dataset:")
print(df)

# Five smallest cities by population

smallest_cities = df.sort_values(
    by="Population_2024"
).head(5)

print("\n5 Smallest Cities:")
print(
    smallest_cities[
        ["City", "Population_2024"]
    ]
)

# Province with highest average growth

province_growth = df.groupby(
    "Province"
)["Growth_Rate"].mean()

print("\nAverage Growth Rate by Province:")
print(province_growth)

highest_growth_province = province_growth.idxmax()

highest_growth_rate = province_growth.max()

print("\nProvince with Highest Average Growth Rate:")
print(highest_growth_province)

print(
    "Average Growth Rate:",
    round(highest_growth_rate, 2),
    "%"
)

# Cities with population above 1 million

cities_above_1_million = df[
    df["Population_2024"] > 1000000
]

number_of_cities = len(cities_above_1_million)

print("\nCities Above 1 Million Population:")

print(
    cities_above_1_million[
        ["City", "Population_2024"]
    ]
)

print(
    "\nNumber of Cities Above 1 Million:",
    number_of_cities
)

# Mean, Median and Difference

mean_population = df["Population_2024"].mean()

median_population = df["Population_2024"].median()

difference = mean_population - median_population

print("\nPopulation Statistics:")

print(
    "Mean Population:",
    round(mean_population, 2)
)

print(
    "Median Population:",
    round(median_population, 2)
)

print(
    "Difference:",
    round(difference, 2)
)

# Explanation

print("\nExplanation:")

print(
    "The mean and median differ because Karachi and Lahore have much larger populations than most other cities, which pulls the mean upward."
)