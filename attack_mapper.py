"""
Script to extract attack data from a CSV file and store it in a SQLite database.
"""

import os  # For file handling
import pandas as pd  # For CSV handling
import sqlite3  # For database storage

# Delete old database if exists
if os.path.exists("attacks.db"):
    print("Old database found. Deleting...")
    os.remove("attacks.db")

# Connect to SQLite database (creates attacks.db if not exists)
conn = sqlite3.connect("attacks.db")
cursor = conn.cursor()

# Create attacks table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS attacks (
        source_ip TEXT,
        destination_ip TEXT,
        destination_port TEXT,
        timestamp TEXT,
        attack_type TEXT
    )
""")
conn.commit()

# Ask for file name
fname = input("Enter CSV file name (hit Enter to use the default 'Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv'): ").strip()

if not fname:  # Use default file if user presses Enter
    fname = "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

# Check if the file exists
if not os.path.exists(fname):
    print(f"Error: The file '{fname}' does not exist in the current directory.")
    exit(1)

# Check if the file has a .csv extension
if not fname.lower().endswith('.csv'):
    print("Error: File must be a .csv")
    exit(1)

# Read the CSV file into a DataFrame
df = pd.read_csv(fname)

# Clean up spaces in headers
df.columns = df.columns.str.strip()

# CSV file information
total = len(df)
benign = (df['Label'] == 'BENIGN').sum()
attacks = total - benign
print(f"Total rows: {total} | BENIGN: {benign} | Attacks: {attacks}")

# Loop through rows
for idx, row in df.iterrows():
    if row['Label'] == "BENIGN": # Skip benign rows
        continue  

    s_ip = row['Source IP']
    d_ip = row['Destination IP']
    d_port = row['Destination Port']
    timestamp = row['Timestamp']
    attack_type = row['Label']

    # Insert each attack into SQLite (inside the loop, correctly)
    cursor.execute("""
        INSERT INTO attacks (source_ip, destination_ip, destination_port, timestamp, attack_type)
        VALUES (?, ?, ?, ?, ?)
    """, (s_ip, d_ip, d_port, timestamp, attack_type))

    # Progress feedback
    if idx % 10000 == 0 and idx > 0:
        print(f"Processed {idx} rows...")

# After loop
if total <= 10000:
    print("Processed all rows.")

conn.commit()
conn.close()
print("Data extraction complete. Database 'attacks.db' created.")