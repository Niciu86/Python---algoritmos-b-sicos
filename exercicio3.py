"""
Funções do pyspark
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,when,avg
spark=SparkSession.builder.appName("Exercício 3").master("local[2]").getOrCreate()
dados=[("Ana",33),("Raul",44),("Iris",22),("Carol",17)]
df=spark.createDataFrame(dados,["nome","idade"])
df.show()
df_novo=df.withColumn("categoria",when(col("idade")>=19,"Adulto").otherwise("menor"))
df_novo.show()
df_final=df_novo.toPandas()
df_final.to_csv("saida_exer3.csv")