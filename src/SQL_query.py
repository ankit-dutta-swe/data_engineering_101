import sqlite3
import pandas as pd

con=sqlite3.connect("/home/ankit/Desktop/data_pipeline_project/data/my_db.db")
query="EXPLAIN ANALYZE SELECT * FROM Employees;"
pdf=pd.read_sql_query(query,con)
print(pdf)