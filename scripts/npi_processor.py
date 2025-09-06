import polars as pl
import pandas as pd
import time

npi_file_path = r'input\NPIFull200505.csv'  # raw string

# just load the first 1000 rows
df_polars = pl.read_csv(npi_file_path, n_rows=1000)

print(f"Successfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"\nDataset shape: {df_polars.shape}")
print(f"\nFirst 5 rows:")
print(df_polars.head())

print(f"\nMemory usage (MB): {df_polars.estimated_size() / 1024**2:.2f}")

df_polars_tiny = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)', 
])

df_polars_tiny = df_polars_tiny.with_columns([
    pl.lit('2025-09-06').alias('last_updated')
])

# rename columns
df_polars_tiny = df_polars_tiny.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
    })

# save to CSV
output_path = r'output\npi_small.csv'  # raw string
df_polars_tiny.write_csv(output_path)

