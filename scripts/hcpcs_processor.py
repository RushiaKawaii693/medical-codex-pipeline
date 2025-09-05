import pandas as pd
from datetime import datetime

# Path to the HCPCS text file
file_path = "input\\HCPC2025_OCT_ANWEB_v2.txt"

def load_hcpcs_to_df(file_path):
    # Adjust colspecs as needed for your file
    colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
    column_names = [
        "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
    ]
    df = pd.read_fwf(file_path, colspecs=colspecs, names=column_names)
    return df

if __name__ == "__main__":
    df = load_hcpcs_to_df(file_path)
    
    # Combine Description1 and Description2 for a full description
    df['description'] = df['Description1'].fillna('') + ' ' + df['Description2'].fillna('')
    df['description'] = df['description'].str.strip()
    
    # Standardize column names
    df_standardized = pd.DataFrame({
        'code': df['Code'],
        'description': df['description'],
        'last_updated': datetime.now().isoformat()
    })
    
    print(df_standardized.head())
    
    # Save as standardized CSV
    output_path = "output\\hcpcs_standardized.csv"
    df_standardized.to_csv(output_path, index=False)
