"""
exercício 4 - ampliado para CSV
"""
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Exercicio 4-1").getOrCreate()
df1=spark.read.csv("ranking_faculdades_tecnologia.csv",header=True,inferSchema=True)
df2=spark.read.csv("rank_faculdades_tecnologia2.csv",header=True,inferSchema=True)
df1.show()
print("======================================================================================")
df2.show()
df_completo=df1.join(df2,on="Nome da Instituição",how="inner")
print("Frame final\n")
df_completo.show()
df_saida=df_completo.toPandas()
df_saida.to_csv("rank_faculdades_tecnologia3.csv")