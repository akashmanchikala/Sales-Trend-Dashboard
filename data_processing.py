import pandas as pd

# Load data
df = pd.read_csv('data/raw_data.csv')

# Clean data
df.dropna(inplace=True)
df['sales'] = df['sales'].astype(float)

# Save cleaned data
df.to_csv('data/cleaned_data.csv', index=False)

print("Data cleaned successfully")
