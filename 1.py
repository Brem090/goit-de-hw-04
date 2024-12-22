from pyspark.sql import SparkSession

# Створюємо сесію Spark
spark = SparkSession.builder \
    .config("spark.sql.shuffle.partitions", "2") \
    .appName("MyGoitSparkSandbox") \
    .getOrCreate()

# Завантажуємо датасет
nuek_df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv('/mnt/f/Educations/goit-de-hw-04/nuek-vuh3.csv')

nuek_repart = nuek_df.repartition(2)

nuek_processed = nuek_repart \
    .where("final_priority < 3") \
    .select("unit_id", "final_priority") \
    .groupBy("unit_id") \
    .count()

# Ось ТУТ додано рядок
nuek_processed = nuek_processed.where("count>2")

nuek_processed.collect()

input("Press Enter to continue...5")

# Закриваємо сесію Spark
spark.stop()
