import pandas as pd

# Sample data containing missing values, a duplicate, and an irrelevant column
data = {
    "Name": ["Asha", "Rohan", "Meera", "Kabir", "Asha"],
    "Marks": [85, 72, None, 90, 85],
    "City": ["Delhi", "Mumbai", "Pune", None, "Delhi"],
    "Remarks": ["Good", "Average", "Good", "Excellent", "Good"]
}
df = pd.DataFrame(data)

# To load your own file, use one of these:
# df = pd.read_csv("students.csv")
# df = pd.read_excel("students.xlsx")
# df = pd.read_excel("students.xls")  # Requires a compatible Excel reader

print("First five rows:")
print(df.head())

print("\nDataFrame information:")
df.info()

print("\nNumeric summary:")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nDuplicate-row flags:")
print(df.duplicated())

df_clean = df.drop_duplicates().copy()

df_clean = df_clean.drop(columns=["Remarks"])

df_clean["Marks"] = df_clean["Marks"].fillna(df_clean["Marks"].median())

city_mode = df_clean["City"].mode()
if not city_mode.empty:
    df_clean["City"] = df_clean["City"].fillna(city_mode.iloc[0])


print("\nCleaned data:")
print(df_clean)

print("\nMissing values after filling:")
print(df_clean.isnull().sum())

# Select columns and filter records using loc[]
selected_columns = df_clean.loc[:, ["Name", "Marks", "City"]]
high_scorers = df_clean.loc[
    df_clean["Marks"] >= 80,
    ["Name", "Marks", "City"]
]

print("\nSelected columns:")
print(selected_columns)

print("\nStudents scoring at least 80:")
print(high_scorers)