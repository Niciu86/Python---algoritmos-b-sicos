from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark=SparkSession.builder.appName("Exercício 7").getOrCreate()
dados_ap=[
    (1,"f",35,"sim",0),
    (2,"m",44,"não",1),
    (3,"f",23,"sim",0),
    (4,"m",38,"não",1),
    (5,"f",15,"sim",0),
    (6,"m",24,"não",1),
]
colunas=["id","sexo","idade","fumante","evasão escolar"]
df_ap=spark.createDataFrame(dados_ap,colunas)
ind_s=StringIndexer(inputCol="sexo",outputCol="sexo_indexado")
ind_f=StringIndexer(inputCol="fumante",outputCol="fumante_indexado")
vet=VectorAssembler(inputCols=["sexo_indexado","idade","fumante_indexado"],outputCol="features")

modelo_ap=LogisticRegression(labelCol="evasão escolar",featuresCol="features")
pipeline=Pipeline(stages=[ind_s,ind_f,vet,modelo_ap])
modelo_final=pipeline.fit(df_ap)
prev_ap=modelo_final.transform(df_ap)
#prev_ap.select("id","fumante","predição","probabilidade").show()
eval_ap=BinaryClassificationEvaluator(labelCol="fumante")
print("AUC:",eval_ap.evaluate(prev_ap))
