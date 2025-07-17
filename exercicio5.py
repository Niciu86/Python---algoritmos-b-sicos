"""
Exercício 5 - ML básico
"""
from PIL.features import features
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.linalg import Vectors
from pyspark.sql import Row
spark=SparkSession.builder.appName("Exercício 5").getOrCreate()
dados=[
    Row(label=3.0,features=Vectors.dense([1.0])),
    Row(label=7.0,features=Vectors.dense([2.0])),
    Row(label=11.0,features=Vectors.dense([3.0]))
]
df=spark.createDataFrame(dados)
rl=LinearRegression()
modelo=rl.fit(df)
print(f"coeficiente: {modelo.coefficients}\n")
print(f"Intercepto: {modelo.intercept}\n")
prev=modelo.transform(df)
prev.show()
