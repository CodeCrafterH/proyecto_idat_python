import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Configuración para limpieza visual de la consola
warnings.filterwarnings("ignore")

# 1. Carga y preparación del dataset
df = pd.read_csv("dataset.txt").dropna()
X = df[['Total Price']] # Variable Predictora
y = df['Units Sold']   # Variable Objetivo

# 2. Entrenamiento del modelo (80% entrenamiento / 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelo = LinearRegression().fit(X_train, y_train)

# 3. Ejecución de resultados y Simulación
r2 = modelo.score(X_test, y_test)
prediccion = modelo.predict([[120]])

print(f"Precisión del modelo (R-squared): {r2:.4f}")
print(f"Predicción para precio S/ 120: {prediccion[0]:.0f} unidades")

# --- 4. SECCIÓN: GRÁFICOS ---

# Configuración del estilo del gráfico
plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

# Para que el gráfico no sea pesado, se tomará una muestra de 2000 datos
df_sample = df.sample(n=min(2000, len(df)), random_state=42)

# Dibujamos los puntos (Ventas Reales) y la Línea de Regresión (Predicción)
sns.regplot(x='Total Price', y='Units Sold', data=df_sample,
    scatter_kws={'alpha':0.5, 'color':'royalblue'},
    line_kws={'color':'red', 'label':'Línea de Tendencia (Modelo)'})

# Personalización de etiquetas y título
plt.title('Modelo de Predicción de Demanda: Precio vs Unidades', fontsize=14, fontweight='bold')
plt.xlabel('Precio Total (S/)', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)

# Mostramos el gráfico
plt.show()