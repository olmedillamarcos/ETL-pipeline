
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

dbutils.widgets.text("filename","")

filename = dbutils.widgets.get("filename")

file_location = f"abfss://json@datalake4213.dfs.core.windows.net/{filename}.json"

spark.conf.set(
    "fs.azure.account.key.datalake4213.dfs.core.windows.net",
    "ywv+PjR+QdEak5AfbLLMecv9fQxj6DQYeZFmh+BuHlSfj7kXgGyd7Y0Se8XjIUMtEi+oEJf6UtLr+ASt52VnIA=="
)


spark = SparkSession.builder.appName("ProcessData").getOrCreate()

# Load data
df = spark.read.json(file_location)

# Your Spark transformations
processed_df = df.withColumn(
    "new", 
    F.explode(F.arrays_zip("hourly.time", "hourly.temperature_2m"))
).select(
    F.col("new.time").alias("time"),
    F.col("new.temperature_2m").alias("temperature_2m")
).withColumn(
    "date",
    F.to_date(F.col("time"))
).select(
    "date",
    "time",
    "temperature_2m"
)

# Write processed data to Parquet
processed_df.write.mode("append").parquet(f"abfss://parquet@datalake4213.dfs.core.windows.net/{filename}.parquet")

# Write to SQL DB
(processed_df.write
  .format("jdbc")
  .option("url", "jdbc:sqlserver://sqlserverolmed.database.windows.net:1433;database=sqldb;")
  .option("dbtable", "testing")
  .option("user", "your_user")
  .option("password", "SQLadmin!")
  .mode("append")
  .save()
)