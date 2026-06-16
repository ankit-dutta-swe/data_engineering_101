import pandas as pd
import sqlite3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

#---------------------
#SQLite DB connection 
#---------------------

conn=sqlite3.connect("/home/ankit/Desktop/data_pipeline_project/data/my_db.db")


#----------------------------
# CREATE PANDAS DATAFRAME (df)
#------------------------------

df=pd.read_sql_query("SELECT * From Employees;",conn)
df1=pd.read_sql_query("SELECT * FROM Bonus;",conn)
conn.close()
print(df1.head())

#--------------------
#CREATE A SPARK SESSION
#--------------------

spark_session=SparkSession.builder.appName("TestSparkSession").getOrCreate()
spark_df=spark_session.createDataFrame(df)   #pandas dataframe to spark dataframe
spark_df1=spark_session.createDataFrame(df1)




#----------------------
#Transform the Data 
#---------------------


spark_df_nt=spark_df.filter(col("salary")>100000)     #narrow transformation
spark_df_nt.explain()


spark_df_wt=spark_df.join(spark_df1, on="id",how="inner").coalesce(4)  #wide transformation
spark_df_wt.explain()


spark_df_nt.show()      #action
spark_df_wt.show()







spark_session.stop()






