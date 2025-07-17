"""
Exercício 2 - Operações com RDD
"""
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("exercicio2").master("local[2]").getOrCreate()
sc=spark.sparkContext
dados_frutas=["banana","maçã","banana","laranja","maçã","banana","uva"]
rdd=sc.parallelize(dados_frutas)
r=rdd.map(lambda x: (x,1)).reduceByKey(lambda a,b:a+b)
r.collect()
sc.stop()