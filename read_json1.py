from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext('local')
spark = SparkSession(sc)
df = spark.read.json("D:\\all-files\\student.json")
df.where("age > 21").select("name.first").show()




