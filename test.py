import pyspark
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
    .appName("PySpark MySQL Example") \
    .config("spark.master", "spark://spark-master:7077") \
    .getOrCreate()

# Configure MySQL connection properties
jdbc_url = "jdbc:mysql://mysql:3306/mydatabase"
connection_properties = {
    "user": "user",
    "password": "userpassword",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Read data from MySQL database into a DataFrame
df = spark.read.jdbc(url=jdbc_url, table="my_table", properties=connection_properties)

# Show DataFrame
df.show()

# Perform SQL queries using SparkSQL
df.createOrReplaceTempView("my_table_view")
result = spark.sql("SELECT * FROM my_table_view WHERE column1 > 10")
result.show()

# Stop SparkSession
spark.stop()
