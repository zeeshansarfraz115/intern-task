import pandas as pd
import numpy as np

# Create the dataset

data = {
    "Name": [
        "Zeeshan", "Hussam", "Basit", "Zain", "Ayesha",
        "Bilal", "Hina", "Usman", "Fatima", "Hamza",
        "Zeeshan", "Basit"
    ],

    "Math": [
        85, 72, 95, 150, 68,
        np.nan, 78, 55, 92, 35,
        85, 95
    ],

    "Science": [
        80, 75, 90, 88, np.nan,
        65, 82, 60, 94, 30,
        80, 90
    ],

    "English": [
        78, 80, 92, 85, 70,
        60, np.nan, 58, 89, 25,
        78, 92
    ],

    "Computer": [
        90, 85, 95, 92, 75,
        70, 88, 65, np.nan, 20,
        90, 95
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Save the dataset as a CSV file

df.to_csv("students_marks.csv", index=False)

print("\nCSV file created successfully!")

# Load the CSV file

df = pd.read_csv("students_marks.csv")

print("\nLoaded Dataset:")
print(df)

# Check for missing values

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values

subjects = ["Math", "Science", "English", "Computer"]

for subject in subjects:
    df[subject] = df[subject].fillna(df[subject].mean())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Find and remove duplicate rows

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df)

# Check and fix invalid marks

for subject in subjects:

    invalid = (df[subject] < 0) | (df[subject] > 100)

    if invalid.any():
        print("\nInvalid marks in", subject)
        print(df.loc[invalid, ["Name", subject]])

        # Replace invalid marks with NaN
        df.loc[invalid, subject] = np.nan

        # Fill invalid marks with subject average
        df[subject] = df[subject].fillna(df[subject].mean())

# Calculate average marks for each student

df["Average"] = df[subjects].mean(axis=1)

print("\nStudent Averages:")
print(df[["Name", "Average"]])

# Find the topper

topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print(topper["Name"])
print("Average:", round(topper["Average"], 2))


# Find the student with the lowest average

lowest = df.loc[df["Average"].idxmin()]

print("\nStudent Needing Most Help:")
print(lowest["Name"])
print("Average:", round(lowest["Average"], 2))

# Calculate subject-wise statistics using NumPy

print("\nSubject-wise Statistics:")

for subject in subjects:

    marks = df[subject].to_numpy()

    mean = np.mean(marks)
    median = np.median(marks)
    standard_deviation = np.std(marks)

    print("\n", subject)
    print("Mean:", round(mean, 2))
    print("Median:", round(median, 2))
    print("Standard Deviation:", round(standard_deviation, 2))

# Add Pass/Fail column
# 40 or above = Pass
# Below 40 = Fail

df["Pass/Fail"] = np.where(
    df["Average"] >= 40,
    "Pass",
    "Fail"
)
print("\nPass/Fail Results:")
print(df[["Name", "Average", "Pass/Fail"]])

# Sort students by average marks

df = df.sort_values(
    by="Average",
    ascending=False
)
print("\nStudents Sorted by Average:")
print(df[["Name"] + subjects + ["Average", "Pass/Fail"]])

# Final Summary

total_students = len(df)
passed_students = (df["Pass/Fail"] == "Pass").sum()
failed_students = (df["Pass/Fail"] == "Fail").sum()

print("\n************************************")
print("          FINAL SUMMARY")
print("**************************************")

print("Total Students:", total_students)
print("Students Passed:", passed_students)
print("Students Failed:", failed_students)

print("\nSubject-wise Class Average:")

for subject in subjects:
    print(
        subject,
        ":",
        round(df[subject].mean(), 2)
    )

print("\nTopper:", topper["Name"])
print("Highest Average:", round(topper["Average"], 2))

print(
    "Student Needing Most Help:",
    lowest["Name"]
)

print(
    "Lowest Average:",
    round(lowest["Average"], 2)
)