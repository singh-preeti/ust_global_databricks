import sqlite3

import pandas as pd
from pandas import DataFrame
import sqlite3 as sql

# ====== Extract ======
df = pd.read_csv("employee.csv")
print("Original Data:")
print(df)

# ====== Transform ======
# Increase salary of IT employees by 10%
df.loc[df['department'] == 'IT', 'salary'] *= 1.10

# Standardize names to uppercase
df['name'] = df['name'].str.upper()

# Add bonus = 5% of salary
df['bonus'] = df['salary'] * 0.05

print("\nTransformed Data:")
print(df)


# ====== Load into SQLite ======
# Connect to SQLite (creates employees.db file if not exists)
conn = sqlite3.connect("employees.db")

# Write DataFrame to SQL table
df.to_sql("employees", conn, if_exists="replace", index=False)

print("\nData has been loaded into employees.db (table: employees)")

# Verify by reading back from database
result = pd.read_sql("SELECT * FROM employees", conn)
print("\nData from DB:")
print(result)

conn.close()
