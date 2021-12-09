
from pyspark.context import SparkContext
import os

os.environ["JAVA_HOME"] = "C:\Program Files (x86)\Java\jre1.8.0_311\\bin"
#os.environ["SPARK_HOME"] = "C:\Spark"

print(os.environ["JAVA_HOME"])
print(os.environ["SPARK_HOME"])

path = "D:\BrowserDownloads\head_pose_inference.json"
sc = SparkContext("local", "myApp")

# df = spark.read.json(path)

peopleDF = sc.read.json(path)

# The inferred schema can be visualized using the printSchema() method
peopleDF.printSchema()

peopleDF.createOrReplaceTempView("people")

# SQL statements can be run by using the sql methods provided by spark
teenagerNamesDF = spark.sql("SELECT name FROM people WHERE age BETWEEN 13 AND 19")
teenagerNamesDF.show()

jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
otherPeopleRDD = sc.parallelize(jsonStrings)
otherPeople = spark.read.json(otherPeopleRDD)
otherPeople.show()
