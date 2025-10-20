from pyspark.sql import SparkSession
import os

from pyspark.sql.functions import col, udf
from pyspark.sql.types import size, LongType


def row_size(*cols):
  return sum([len(str(c).encode('utf-8')) for c in cols])

def main():
    spark = (
        SparkSession.builder
        .appName("PySpark Demo")
        .getOrCreate()
    )

    print(f"Spark version: {spark.version}")
    print(f"JAVA_HOME: {os.getenv('JAVA_HOME')}")

    df = spark.read.csv("../data/products-100000.csv", header=True, inferSchema=True)
    row_size_udf = udf(row_size, LongType())
    df_with_size = df.withColumn("row_size", row_size_udf(*df.columns))
    df_with_size.show(10)
    spark.stop()

if __name__ == "__main__":
    main()