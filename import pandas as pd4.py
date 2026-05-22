import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Importar los datos y establecer la columna 'date' como índice
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# 2. Limpiar los datos filtrando los días en los percentiles extremos (top 2.5% y bottom 2.5%)
df = df[
    (df["value"] >= df["value"].quantile(0.025)) &
    (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Copiar el DataFrame original
    df_line = df.copy()

    # Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # Dibujar el gráfico de líneas
    ax.plot(df_line.index, df_line["value"], color="red", linewidth=1)
    
    # Título y etiquetas de los ejes
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    # Guardar la imagen y retornarla (No modificar)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copiar y preparar los datos para el gráfico de barras
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.strftime("%B")

    # Agrupar por año y mes calculando el promedio diario de visitas
    df_grouped = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    # Ordenar las columnas para que los meses sigan el orden cronológico estricto
    months_order = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    df_grouped = df_grouped.reindex(columns=months_order)

    # Dibujar el gráfico de barras agrupadas
    fig = df_grouped.plot(kind="bar", figsize=(7, 7)).get_figure()
    
    # Configurar títulos, etiquetas y leyenda según las reglas del test
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=months_order)

    # Guardar la imagen y retornarla (No modificar)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Copiar y preparar los datos para los diagramas de caja (Ya configurado en el boilerplate)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Configurar la estructura para dos subgráficos uno al lado del otro
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Orden cronológico abreviado para el gráfico de estacionalidad mensual
    month_order_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    # Gráfico 1: Por Año (Tendencia)
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0], palette="tab10")
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Gráfico 2: Por Mes (Estacionalidad)
    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=month_order_short, palette="husl")
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Guardar la imagen y retornarla (No modificar)
    fig.savefig('box_plot.png')
    return fig