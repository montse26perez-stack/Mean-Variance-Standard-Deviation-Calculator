import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar los datos desde el archivo CSV
df = pd.read_csv('medical_examination.csv')

# 2. Agregar la columna 'overweight' (sobrepeso)
# Fórmula BMI = peso (kg) / [altura (m)]^2. Pasamos altura de cm a metros dividiendo por 100.
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalizar datos: 0 siempre es bueno, 1 siempre es malo (para cholesterol y gluc)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Dibujar el Gráfico Categórico
def draw_cat_plot():
    # 5. Crear el DataFrame para el cat plot usando pd.melt
    df_cat = pd.melt(
        df, 
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Agrupar y reformatear los datos para mostrar los conteos ('total')
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Convertir los datos a formato largo y crear el gráfico con sns.catplot()
    chart = sns.catplot(
        x='variable', 
        y='total', 
        hue='value', 
        col='cardio', 
        data=df_cat, 
        kind='bar'
    )
    
    # 8. Obtener la figura para la salida
    fig = chart.fig

    # 9. No modificar las siguientes dos líneas
    fig.savefig('catplot.png')
    return fig


# 10. Dibujar el Mapa de Calor (Heat Map)
def draw_heat_map():
    # 11. Limpiar los datos en df_heat filtrando los segmentos incorrectos/extremos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcular la matriz de correlación
    corr = df_heat.corr()

    # 13. Generar una máscara para el triángulo superior (para que no se repitan los datos en espejo)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Graficar la matriz usando sns.heatmap() con el formato que exige el test
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt=".1f", 
        cmap='coolwarm', 
        square=True, 
        linewidths=0.5, 
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    # 16. No modificar las siguientes dos líneas
    fig.savefig('heatmap.png')
    return fig