import pandas as pd

# 1. Carga de datos
df = pd.read_csv("dataset.txt")

# 2. Ingeniería de Variables: Calculamos el % de descuento real
# Esto responde al "Dolor" de la empresa
df['Descuento_Pct'] = (df['Base Price'] - df['Total Price']) / df['Base Price']

# 3. Limpieza: Eliminamos registros donde el precio sea 0 o negativo (errores de sistema)
df = df[df['Total Price'] > 0]

print("Resumen inicial del Dataset:")
print(df[['Total Price', 'Base Price', 'Units Sold', 'Descuento_Pct']].describe())

