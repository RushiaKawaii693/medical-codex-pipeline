import pandas as pd

# Replace 'your_data.csv' with your actual file path
data = pd.read_csv('input\Loinc.csv')

# Check if the data loaded correctly
print(data.head())
