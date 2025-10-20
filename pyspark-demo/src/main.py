from pyspark.sql import SparkSession
import os

def main():
    spark = (
        SparkSession.builder
        .appName("PySpark Demo")
        .getOrCreate()
    )

    print(f"Spark version: {spark.version}")
    print(f"JAVA_HOME: {os.getenv('JAVA_HOME')}")

    df = spark.read.csv("../data/products-100000.csv", header=True, inferSchema=True)
    df.show(5)
    # Investigate files archiving into avro, parquet, orc etc..
    spark.stop()

if __name__ == "__main__":
    main()