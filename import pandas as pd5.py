import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar los datos desde epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crear el diagrama de dispersión (Scatter Plot)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Datos Originales', s=10)

    # 3. Primera línea de mejor ajuste (Todos los datos: 1880 - 2050)
    # Obtener pendiente (slope) e intersección (intercept)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Crear una secuencia de años extendida hasta 2050
    years_all = pd.Series([i for i in range(1880, 2051)])
    # Calcular los valores correspondientes de Y usando la ecuación de la recta: y = mx + b
    sea_levels_all = res_all.slope * years_all + res_all.intercept
    
    # Graficar la primera línea de predicción
    plt.plot(years_all, sea_levels_all, color='red', label='Ajuste (1880-2050)', linestyle='--')

    # 4. Segunda línea de mejor ajuste (Datos recientes: 2000 - 2050)
    # Filtrar el dataframe original para conservar solo desde el año 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Crear una secuencia de años desde 2000 hasta 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    # Calcular los nuevos valores de Y con la pendiente acelerada
    sea_levels_recent = res_recent.slope * years_recent + res_recent.intercept
    
    # Graficar la segunda línea de predicción
    plt.plot(years_recent, sea_levels_recent, color='green', label='Ajuste (2000-2050)')

    # 5. Configurar títulos y etiquetas exactas exigidas por el test
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Guardar la imagen y retornarla (No modificar el bloque final)
    plt.savefig('sea_level_plot.png')
    return plt.gca()