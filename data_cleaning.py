import pandas as pd

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# View first 5 rows
print(df.head())

# Check dataset info
print(df.info())

# Check shape
print(df.shape)

# ==============================
# Step 2: Handle Missing Values
# ==============================

# BEFORE cleaning
print("\nMissing values BEFORE cleaning:")
print(df.isnull().sum())

# Fill missing categorical values
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Not Available')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Unknown')

# Drop rows with missing date
df = df.dropna(subset=['date_added'])

# AFTER cleaning
print("\nMissing values AFTER cleaning:")
print(df.isnull().sum())

# Step 3: Remove duplicate rows
df = df.drop_duplicates()

# Step 4: Standardize column names
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Step 5: Convert date_added to datetime
df = df.dropna(subset=['date_added'])


# Save cleaned dataset
df.to_csv("cleaned_netflix_data.csv", index=False)
print("\nCleaned dataset saved successfully!")


