"""
Exercício 6 - Groupby, join, agg
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum as _sum

spark=SparkSession.builder.appName("Exercício 6").getOrCreate()
clientes_novo=[(1,"Ana","RJ"),(2,"Iris","SP"),(3,"Carlos","MG"),(4,"Raul","PE")]
df_clientes_n=spark.createDataFrame(clientes_novo,["id","nome","estado"])
df_clientes_n.show()
vendas=[(1,140),(2,450),(2,500),(3,900),(4,489),(3,100),(4,899),(1,50)]
df_v=spark.createDataFrame(vendas,["id","valor"])
df_v.show()
df_t=df_v.groupBy("id").agg(_sum("valor").alias("total"))
df_t.show()
relatorio=df_clientes_n.join(df_t,on="id",how="inner")
#relatorio.show()
relatorio.select("nome","estado","total").orderBy("total",ascending=True).show()
df_resul=relatorio.toPandas()
df_resul.to_csv("saida_exer6.csv")
