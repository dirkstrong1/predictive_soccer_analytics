import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql:///soccer_database')

df = pd.read_sql_query('SELECT * FROM epl_2008 LIMIT 5;', engine)

print(df)