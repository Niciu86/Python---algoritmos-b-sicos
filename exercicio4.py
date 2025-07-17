"""
Exercício 4 - Joins no pyspark
"""
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Exercício 4").getOrCreate()
clientes=[(1,"Ana"),(2,"Raul"),(3,"Carol"),(4,"Carlos")]
compras=[(1,"Livro"),(2,"DVD-player"),(3,"Celular"),(4,"Notebook")]
total=[(1,100),(2,250),(3,500),(4,5000)]
df_cliente=spark.createDataFrame(clientes,["id","nome"])
df_compras=spark.createDataFrame(compras,["id","produto"])
df_total=spark.createDataFrame(total,["id","custo total"])
df_cliente.show()
df_compras.show()
df_total.show()
df_completo=df_cliente.join(df_compras,on="id",how="inner")
df_completo.show()
df_completo_final=df_completo.join(df_total,on="id",how="inner")
df_completo_final.show()
df_final=df_completo_final.toPandas()
df_final.to_csv("saida_exer4.csv")