"""
Exercício 1 - leitura e operação com DataFrame
"""
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("Exercicio 1").master("local[3]").getOrCreate()
df=spark.read.csv("ranking_faculdades_tecnologia.csv",header=True,inferSchema=True)
df.printSchema()
df.show()
print("--------------------------------------------------------------------------------")
df_sel=df.select("Nome","País","Ano de Fundação").where(df["Ano de Fundação"]>1990)
df_sel.show(1000)
df_ag=df_sel.groupby("País").count()
df_ag.show()
df_final=df_ag.toPandas()
df_final.to_csv("saida.csv")