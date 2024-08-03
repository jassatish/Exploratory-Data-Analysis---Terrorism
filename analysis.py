# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual settings
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

# Step 2: Load the Dataset
df = pd.read_csv('globalterrorismdb_0718dist.csv', encoding='ISO-8859-1')

# Display the first few rows of the dataset
print(df.head())

# Step 3: Data Cleaning
# Check for missing values
missing_values = df.isnull().sum()
print("Missing values in each column:\n", missing_values)

# Handle missing values by filling them with 'Unknown' for categorical and 0 for numerical data
df.fillna({
    'country_txt': 'Unknown',
    'region_txt': 'Unknown',
    'attacktype1_txt': 'Unknown',
    'iyear': 0,
    'imonth': 0,
    'iday': 0,
    'nkill': 0,
    'nwound': 0
}, inplace=True)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")

# Step 4: Basic Statistics
# Get basic statistics
print(df.describe())

# Unique values in critical columns
print("Unique countries:", df['country_txt'].nunique())
print("Unique regions:", df['region_txt'].nunique())
print("Unique attack types:", df['attacktype1_txt'].nunique())

# Step 5: Visualization

# Terrorist attacks over the years
plt.figure(figsize=(15, 8))
sns.countplot(x='iyear', data=df, palette='viridis')
plt.title('Number of Terrorist Attacks Over Years')
plt.xlabel('Year')
plt.ylabel('Number of Attacks')
plt.xticks(rotation=90)
plt.show()

# Terrorist attacks by region
plt.figure(figsize=(15, 8))
sns.countplot(y='region_txt', data=df, order=df['region_txt'].value_counts().index, palette='viridis')
plt.title('Number of Terrorist Attacks by Region')
plt.xlabel('Number of Attacks')
plt.ylabel('Region')
plt.show()

# Terrorist attacks by country (Top 10)
plt.figure(figsize=(15, 8))
top_countries = df['country_txt'].value_counts().head(10)
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Top 10 Countries with Most Terrorist Attacks')
plt.xlabel('Number of Attacks')
plt.ylabel('Country')
plt.show()

# Terrorist attacks by attack type
plt.figure(figsize=(15, 8))
sns.countplot(y='attacktype1_txt', data=df, order=df['attacktype1_txt'].value_counts().index, palette='viridis')
plt.title('Terrorist Attacks by Type')
plt.xlabel('Number of Attacks')
plt.ylabel('Attack Type')
plt.show()

# Step 6: Insights
# Hot Zones of Terrorism
hot_zones = df['country_txt'].value_counts().head(10)
print("Top 10 Hot Zones of Terrorism:\n", hot_zones)

# Attack Trends Over the Years
attack_trends = df['iyear'].value_counts().sort_index()
print("Attack Trends Over the Years:\n", attack_trends)

# Common Types of Attacks
common_attacks = df['attacktype1_txt'].value_counts().head(5)
print("Most Common Types of Attacks:\n", common_attacks)

# Summary of Security Issues and Insights
print("""
Security Issues and Insights:
1. The Middle East & North Africa and South Asia are prominent hot zones for terrorist activities.
2. Countries like Iraq, Afghanistan, and Pakistan face the highest number of attacks, indicating significant security concerns.
3. The number of terrorist attacks has shown fluctuations over the years, with noticeable peaks during certain periods.
4. Bombings and armed assaults are the most common types of attacks, suggesting vulnerabilities in public safety and surveillance systems.
5. Effective counter-terrorism measures, political stability, and enhanced security protocols are critical to mitigating these threats.
""")
