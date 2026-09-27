import pandas as pd
from sqlalchemy import create_engine

# Database Connection Details
user = 'root'            # your MySQL username (e.g., root)
password = '' # your MySQL password
host = 'localhost'       # host name (e.g., localhost or 127.0.0.1)
port = '3306'            # MySQL default port
database = 'footballer'  # database name

# SQLAlchemy Engine creation
connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# SQL Query run and load into Pandas DataFrame
query = "SELECT * FROM players;"
df = pd.read_sql(query, con=engine)

# DataFrame to SQL table
print(df)