#!/usr/bin/env bash

# --- spark-env.sh ---
# Custom environment for Spark runtime

# Path to your Spark installation
export SPARK_HOME="$HOME/spark-3.5.1-bin-hadoop3"

# Ensure Java 17 is used
export JAVA_HOME=" /Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home"

# Optional: Python version to use
export PYSPARK_PYTHON=$(which python3)

# Optional: tuning
export SPARK_LOCAL_IP="127.0.0.1"
export SPARK_DRIVER_MEMORY="2g"

echo "Using JAVA_HOME=${JAVA_HOME}"
echo "Using PYSPARK_PYTHON=${PYSPARK_PYTHON}"