import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
from dash import Input, Output

# Dataset
df = px.data.iris()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Ejemplo: Gráfico con Dash y Plotly"),
    dcc.Graph(
        id="grafico-iris",
        figure=px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    )
])

app.layout = html.Div([
    html.H1("Filtrar especie"),
    dcc.Dropdown(
        id="dropdown-especie",
        options=[{"label": sp, "value": sp} for sp in df["species"].unique()],
        value="setosa"
    ),
    dcc.Graph(id="grafico-filtrado")
])

@app.callback(
    Output("grafico-filtrado", "figure"),
    Input("dropdown-especie", "value")
)
def actualizar_grafico(especie):
    df_filtrado = df[df["species"] == especie]
    fig = px.scatter(df_filtrado, x="sepal_width", y="sepal_length", color="species")
    return fig

if __name__ == "__main__":
    app.run(debug=True, port=8088)
