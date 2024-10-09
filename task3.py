from pyspark.sql import SparkSession, DataFrame

spark = SparkSession.builder.getOrCreate()

table: DataFrame = spark.read.csv('./table.csv', header=True)
table.show()