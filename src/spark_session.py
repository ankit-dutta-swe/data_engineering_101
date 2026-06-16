from pyspark.sql import SparkSession
# spark=SparkSession.builder.appName("ETL Pipeline").getOrCreate()
# df=spark.read.csv('/home/ankit/Desktop/data_pipeline_project/data/family.csv')
# df.head()
# from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("TestSpark")
    .master("local[2]")
    .config("spark.jars","/path/to/sqlite-jdbc-3.50.3.0.jar")
    .getOrCreate()
)

df=spark.read.csv("/home/ankit/Desktop/data_pipeline_project/data/family.csv")
print("Spark Version:", spark.version)
print(type(df))
df.show()
spark.stop()


