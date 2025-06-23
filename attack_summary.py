"""
Script to analyse attack data stored in a SQLite database and generate a summary report.
"""
import os
import sqlite3
import pandas as pd

# Check if the database file exists
if not os.path.isfile("attacks.db"):
    print("Error: 'attacks.db' not found. Please run attack_analyzer.py first.")
    exit(1)

# Connect to existing attacks.db
conn = sqlite3.connect("attacks.db")
cursor = conn.cursor()

# Load data from the attacks table into a DataFrame
df = pd.read_sql_query("SELECT * FROM attacks", conn)

# Check if table is empty
if df.empty:
    print("No data found in 'attacks' table. Please run the attack mapper script first.")
    exit(1)

# --- Summary Section ---
print("Summary Report")

top_n = 10  # Number of top results to display in each category

# 1. Top Attacking IPs
print(f"\nTop {top_n} Attacking IPs:")
query = """
    SELECT source_ip, COUNT(*) as count
    FROM attacks
    GROUP BY source_ip
    ORDER BY count DESC
    LIMIT ?
"""
cursor.execute(query, (top_n,))
rows = cursor.fetchall()
for ip, count in rows:
    print(f"{ip:<20} {count} attacks")

print("\nTop Attack Types:")

# 2. Top Attack Types
query = """
    SELECT attack_type, COUNT(*) as count
    FROM attacks
    GROUP BY attack_type
    ORDER BY count DESC
    LIMIT ?
"""
cursor.execute(query, (top_n,))
rows = cursor.fetchall()

for attack_type, count in rows:
    print(f"{attack_type:<20} {count} occurrences")

# 3. Timeline of Attacks
print("\nTimeline of Attacks (per hour):")
query = """
    SELECT 
        SUBSTR(timestamp, 1, 13) AS hour,
        COUNT(*) as count
    FROM attacks
    GROUP BY hour
    ORDER BY hour
"""
cursor.execute(query)
rows = cursor.fetchall()

for hour, count in rows:
    print(f"{hour}:00 - {count} attacks")


# 4. Most Targeted Ports
print(f"\nTop {top_n} Targeted Ports:")
query = """
    SELECT destination_port, COUNT(*) as count
    FROM attacks
    GROUP BY destination_port
    ORDER BY count DESC
    LIMIT ?
"""
cursor.execute(query, (top_n,))
rows = cursor.fetchall()

for destination_port, count in rows:
    print(f"{destination_port:<20} {count} occurrences")

# Close connection
conn.close()