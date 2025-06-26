import dash
from dash import dcc, html
import plotly.graph_objs as go

# carregar previsões e históricos
df_historico = df.copy()
df_previsao = df_resultados.copy()
df_previsao["Previsão Comissão"] = pd.to_numeric(df_previsao["Previsão Comissão"].str.replace("R$", "").str.replace(",", "."), errors='coerce')

app = dash.Dash(__name__)
app.title = "Dashboard de Previsões de Comissão"

# opções únicas
seguradoras = sorted(df_previsao["Seguradora"].unique())
produtos = sorted(df_previsao["Produto"].unique())

app.layout = html.Div([
    html.H1("📊 Previsão de Comissões por Seguradora e Produto"),
    
    html.Label("Seguradora:"),
    dcc.Dropdown(
        id="dropdown-seguradora",
        options=[{"label": s, "value": s} for s in seguradoras],
        value=seguradoras[0]
    ),

    html.Label("Produto:"),
    dcc.Dropdown(
        id="dropdown-produto",
        options=[{"label": p, "value": p} for p in produtos],
        value=produtos[0]
    ),

    dcc.Graph(id="grafico-comparativo"),
])

@app.callback(
    dash.dependencies.Output("grafico-comparativo", "figure"),
    [
        dash.dependencies.Input("dropdown-seguradora", "value"),
        dash.dependencies.Input("dropdown-produto", "value"),
    ]
)
def atualizar_grafico(seguradora, produto):
    # histórico
    historico = df_historico[(df_historico["Seguradora"] == seguradora) & (df_historico["Produto"] == produto)]
    historico_agrupado = historico.groupby("Data de Emissão")["Valor Comissão"].sum().reset_index()

    # previsão
    previsao = df_previsao[(df_previsao["Seguradora"] == seguradora) & (df_previsao["Produto"] == produto)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=historico_agrupado["Data de Emissão"],
        y=historico_agrupado["Valor Comissão"],
        mode="lines+markers",
        name="Histórico"
    ))

    fig.add_trace(go.Scatter(
        x=previsao["Data"],
        y=previsao["Previsão Comissão"],
        mode="lines+markers",
        name="Previsão"
    ))

    fig.update_layout(
        title=f"{seguradora} - {produto}",
        xaxis_title="Data",
        yaxis_title="Comissão (R$)",
        template="plotly_white"
    )

    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
