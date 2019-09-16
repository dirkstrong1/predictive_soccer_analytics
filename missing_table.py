import pandas as pd
import sqlite3
from sqlalchemy import create_engine

#connect with a database 
conn = sqlite3.connect('soccer_database.sqlite')

#convert a table from sqlite database to pandasframe
df = pd.read_sql_query('SELECT * FROM player', conn)

#add a dataframe to postgresql
engine = create_engine('postgresql:///soccer_database')
df.to_sql("player", engine, if_exists = 'replace')
