from dash import Dash, html, dcc, callback, Output, Input
import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from .sidebar import sidebar
import dash_bootstrap_components as dbc

df = pd.read_csv("data/sales.csv", nrows=1_000)

dash.register_page(__name__, path='/dashboard')

layout = [ 
    html.Div(
        className="app-header-bar",
        children = [
            html.H1("Data analytics dashboard"),
            dbc.Row(
                [dbc.Col(sidebar(), width=2)]
            )
        ],
    ),
    html.Div(
        className="app-header",
        children=[
            html.Img(src='/assets/logo.jpeg', alt='Casino Avalillo'),
            html.H1("Graficos a mostrar")
        ]
    ),
    html.Div(
        className="app-info",
        children=[
            html.Div(
                className="app-info-card",
                children=[ html.H2("297"), html.H4("Total Global") ],
                style={'background-color': '#5c59a7'}
            ),
            html.Div(
                className="app-info-card",
                children=[ html.H2("297"), html.H4("Total Global") ],
                style={'background-color': '#e65541'}
            ),
            html.Div(
                className="app-info-card",
                children=[ html.H2("297"), html.H4("Total Global") ],
                style={'background-color': '#00a859'}
            ),
            html.Div(
                className="app-info-card",
                children=[ html.H2("297"), html.H4("Total Global") ],
                style={'background-color': '#4da6d1'}
            )
        ]
    ),
    html.Div(
        className="app-main",
        children=[
            html.Div(
                className="app-main-card",
                children=[
                    html.Div( 
                        className="app-main-card-title", 
                        children=[ html.H3("Participaciones por zona") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div( 
                        className="app-main-card-body", 
                        children=[ dcc.Graph(figure=px.histogram(df, x='Country', y='Total Revenue', histfunc='avg')) ]
                    ),
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div( 
                        className="app-main-card-title", 
                        children=[ html.H3("Participaciones por zona") ],
                        style={'background-color': '#00c1f3'}
                    ),
                    html.Div( 
                        className="app-main-card-body", 
                        children=[ dcc.Graph(figure=px.histogram(df, x='Country', y='Total Revenue', histfunc='avg')) ]
                    ),
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div( 
                        className="app-main-card-title", 
                        children=[ html.H3("Participaciones por zona") ],
                        style={'background-color': '#f7941d'}
                    ),
                    html.Div( 
                        className="app-main-card-body", 
                        children=[ dcc.Graph(figure=px.histogram(df, x='Country', y='Total Revenue', histfunc='avg')) ]
                    ),
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div( 
                        className="app-main-card-title", 
                        children=[ html.H3("Participaciones por zona") ],
                        style={'background-color': '#00a859'}
                    ),
                    html.Div( 
                        className="app-main-card-body", 
                        children=[ dcc.Graph(figure=px.histogram(df, x='Country', y='Total Revenue', histfunc='avg')) ]
                    ),
                ]
            ),
        ]
    ),
    dag.AgGrid(
        rowData = df.to_dict('records'),
        columnDefs = [ {"field": i} for i in df.columns]
    ),

    dcc.RadioItems(options=['Unit Price', 'Unit Cost', 'Units Sold'], value='Units Sold', id='controls-radio-item'),
    dcc.Graph(figure={}, id='controls-graph')
]

@callback(
    Output(component_id='controls-graph', component_property='figure'),
    Input(component_id='controls-radio-item', component_property='value')
)
def update_graph(col_choosen):
    fig = px.histogram(df, x='Region', y=col_choosen, histfunc='avg')
    return fig