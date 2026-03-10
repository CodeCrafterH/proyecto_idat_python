import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd


df = pd.read_csv("dataset.txt")

X = df[['Total Price']]
y = df['Units Sold']

# 2.2 Gráfico de Comparación (Elasticidad)
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Total Price', y='Units Sold', alpha=0.5)
plt.title("Análisis de Elasticidad: Precio vs Unidades")
plt.show()

# 2.3 Gráfico Segmentado (Ventas por Tienda)
tiendas_top = df.groupby('Store ID')['Units Sold'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,5))
tiendas_top.plot(kind='bar', color='teal')
plt.title("Segmentación: Top 10 Tiendas por Volumen")
plt.ylabel("Unidades Totales")
plt.show()