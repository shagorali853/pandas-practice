import sqlite3
import pandas as pd

# create demonstration data
data = {
    'Name': ['Rahim', 'Karim', 'Sadia'],
    'Age': [25, 30, 22],
    'City': ['Dhaka', 'Chittagong', 'Sylhet']
}
df = pd.DataFrame(data)

# database connection
conn = sqlite3.connect('my_database.db')

# DataFrame to SQL table
df.to_sql('users', conn, if_exists='replace', index=False)

print("Data saved successfully!")
conn.close()