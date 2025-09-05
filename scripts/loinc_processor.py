import pandas as pd
from datetime import datetime

# Load the data
data = pd.read_csv('input\Loinc.csv')

data.info()  # Check the structure of the DataFrame

# Standardize column names
data = data.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description'
})

# Add last_updated column
data['last_updated'] = datetime.now().isoformat()

# Check the result
print(data[['code', 'description', 'last_updated']].head())


# Save the standardized DataFrame to a new CSV file
data[['code', 'description', 'last_updated']].to_csv('output\loinc_standardized.csv', index=False)