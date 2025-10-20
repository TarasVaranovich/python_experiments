import os

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import LongType

from functions import row_to_product


def row_size(*cols):
  return sum([len(str(c).encode('utf-8')) for c in cols])


# def merge(acc: list[Product], entry: Product):
#   count = acc.count + 1
#   sum = acc.sum + x
#   return struct(count.alias("count"), sum.alias("sum"))


def main():
  spark = (
    SparkSession.builder
    .appName("PySpark Demo")
    .getOrCreate()
  )

  print(f"Spark version: {spark.version}")
  print(f"JAVA_HOME: {os.getenv('JAVA_HOME')}")

  df = spark.read.csv("../data/products-100000.csv", header=True,
                      inferSchema=True)
  row_size_udf = udf(row_size, LongType())
  df_with_size = df.withColumn("row_size", row_size_udf(*df.columns))
  print("Enriched with row size:")
  df_with_size.show(10)
  typed_df = df_with_size.rdd.map(lambda row: row_to_product(row))
  print("Converted into class - columns in unexpected order:")
  typed_df.toDF().show()
  max_size = typed_df.max(key=lambda p: p.row_size)
  print("Max row size:")
  print(max_size.row_size)
  min_size = typed_df.min(key=lambda p: p.row_size)
  print("Min row size:")
  print(min_size.row_size)
  spark.stop()


if __name__ == "__main__":
  main()
