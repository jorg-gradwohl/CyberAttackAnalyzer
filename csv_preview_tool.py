"""
Utility script to preview structure and sample data from large CSV files used in cybersecurity projects.
"""

import pandas as pd

# Ask for file name
fname = input("Enter CSV file name: ").strip()
if not fname:
    fname = "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

# Check if file exists
try:
    df = pd.read_csv(fname)
except FileNotFoundError:
    print(f"Error: File '{fname}' not found.")
    exit(1)

# Ask for how many colums to show
col_input = input("Enter number of Column Headers to show (default 10): ").strip()
num_cols = int(col_input) if col_input.isdigit() else 10

# Clean up spaces in headers
df.columns = df.columns.str.strip()  

# Print summary
print("\n CSV Overview")
print(f" Total Rows: {len(df):,}")
print(f" Total Columns: {len(df.columns)}")

# Print column headers
print("\n Column Headers:")
for i, col in enumerate(df.columns[:num_cols], start=1):
    print(f"   {i}. {col}")
if len(df.columns) > num_cols:
    print("   ...")

# Showing small sample data
print("\n Sample Data (first 3 rows, first 6 columns):")
print(df.iloc[:3, :6].to_string(index=False))

sel_col = input("\nTo display sample data of a specific column, enter column number. Press Enter to skip: ").strip()

if sel_col.isdigit():
    sel_col = int(sel_col) - 1
    if 0 <= sel_col < len(df.columns):
        print(f"\nDisplaying column {sel_col+1}: {df.columns[sel_col]}")
        print(df.iloc[:10, sel_col].to_string(index=False))
    else:
        print("Invalid column index.")
elif sel_col:
    print("Input not recognized. Please enter a number or press Enter to quit.")


