import pandas as pd

# File Paths
input_file = 'C:\\Users\\Acer\\Desktop\\iVedha_assignment\\assignment_data.csv'
output_file = 'C:\\Users\\Acer\\Desktop\\iVedha_assignment\\filtered-sales-data.csv'

# Load Data
df = pd.read_csv(input_file)

# Print Columns
print(df.columns)

# Calculate Average Price per Square Foot
df['price_per_sq_ft'] = df['price'] / df['sq__ft']
average_price_per_sqft = df['price_per_sq_ft'].mean()

# Filter Data
filtered_df = df[df['price_per_sq_ft'] < average_price_per_sqft]

# Save Filtered Data
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
