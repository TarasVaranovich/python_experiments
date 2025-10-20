#!/usr/bin/env bash
# --- spark-env.sh ---
# Auto-detect PySpark & Java 17 environment setup
#  /Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home
# Try to detect Spark installation path dynamically
if [ -z "$SPARK_HOME" ]; then
  # Case 1: pip-installed PySpark
  PYSPARK_PATH=$(python3 -c "import pyspark, os; print(os.path.dirname(pyspark.__file__))" 2>/dev/null)
  if [ -n "$PYSPARK_PATH" ]; then
    export SPARK_HOME="$PYSPARK_PATH"
  else
    # Case 2: system Spark (installed manually)
    SPARK_BIN=$(command -v pyspark)
    if [ -n "$SPARK_BIN" ]; then
      export SPARK_HOME=$(dirname "$(dirname "$SPARK_BIN")")
    else
      echo "⚠️  Could not detect Spark installation. Please set SPARK_HOME manually."
    fi
  fi
fi

# --- Java 17 setup ---
# Try to detect Java 17 automatically, or fall back to manual path
if [ -z "$JAVA_HOME" ]; then
  if [ -d "/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home" ]; then
    export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home"
  elif [ -d "/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home" ]; then
    export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-17.0.4.jdk/Contents/Home"
  elif command -v /usr/libexec/java_home &>/dev/null; then
    export JAVA_HOME=$(/usr/libexec/java_home -v 17 2>/dev/null)
  else
    echo "⚠️  Java 17 not found. Please install it and update JAVA_HOME."
  fi
fi

# Add to PATH
export PATH="$JAVA_HOME/bin:$SPARK_HOME/bin:$PATH"

# Python interpreter
export PYSPARK_PYTHON=$(command -v python3)

# Optional Spark memory configs
export SPARK_DRIVER_MEMORY="2g"

echo "✅ SPARK_HOME = $SPARK_HOME"
echo "✅ JAVA_HOME  = $JAVA_HOME"
echo "✅ PYTHON     = $PYSPARK_PYTHON"