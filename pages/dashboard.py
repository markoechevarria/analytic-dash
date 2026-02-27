from dash import Dash, html, dcc, callback, Output, Input
import dash
import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from .sidebar import sidebar
import dash_bootstrap_components as dbc

df = pd.read_csv("data/sales.csv", nrows=1_000)

figBarras = px.histogram(
    df[df["Country"].str.startswith('A')],
    x='Country',
    y='Total Revenue',
    labels={ "Country": "Pais", "Total Revenue": "Ingresos Totales" },
    histfunc='avg'
)
figBarras.update_layout( autosize=True, font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=35, b=10) )
figBarras.update_traces(textfont_color="white")

dfpie = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
dfpie.loc[dfpie['pop'] < 3.e6, 'country'] = 'Other countries'
figPie = px.pie(
    dfpie,
    values='pop',
    names='country',
)
figPie.update_layout(autosize=True,  font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=35, b=10) )

figCuadro = px.treemap(
    px.data.gapminder().query("year == 2007"),
    path=[px.Constant('world'), 'continent', 'country'],
    values='pop',
    color='lifeExp',
    hover_data=['iso_alpha']
)
figCuadro.update_layout(autosize=True, font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=10, r=10, t=35, b=10) )

figMapa = px.scatter_geo(
    px.data.gapminder(),
    locations="iso_alpha",
    color="continent",
    hover_name="country",
    size="pop",
    animation_frame="year",
    projection="natural earth"
)
figMapa.update_layout(autosize=True, font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=0, b=0), height=500, )
figMapa.update_geos( bgcolor='rgba(0,0,0,0)', showframe=False, showcoastlines=True, projection_type="natural earth", coastlinecolor="rgba(255,255,255,0.2)", visible=True, resolution=50, projection_scale=1.2)

figGlobo = px.scatter(
    px.data.gapminder().query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
figGlobo.update_layout(autosize=True, font_color="white", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0, r=0, t=0, b=0), height=500, )


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
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-main-card-body",
                        children=[ dcc.Graph(
                            figure= px.treemap(
                                px.data.gapminder().query("year == 2007"),
                                path=[px.Constant('world'), 'continent', 'country'],
                                values='pop',
                                color='lifeExp',
                                hover_data=['iso_alpha']
                            ))
                        ]
                    ),
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div(
                        className="app-main-card-title",
                        children=[ html.H3("Ingresos totales por pais que inician con A") ],
                        style={'background-color': '#00c1f3'}
                    ),
                    html.Div(
                        className="app-main-card-body",
                        children=[ dcc.Graph(
                            figure=px.histogram(
                                df[df["Country"].str.startswith('A')],
                                x='Country',
                                y='Total Revenue',
                                labels={ "Country": "Pais", "Total Revenue": "Ingresos Totales" },
                                histfunc='avg'
                            ) )
                        ]
                    )
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div(
                        className="app-main-card-title",
                        children=[ html.H3("Poblacion por Pais") ],
                        style={'background-color': '#f7941d'}
                    ),
                    html.Div(
                        className="app-main-card-body",
                        children=[ dcc.Graph(
                            figure=px.scatter_geo(
                                px.data.gapminder(),
                                locations="iso_alpha",
                                color="continent",
                                hover_name="country",
                                size="pop",
                                animation_frame="year",
                                projection="natural earth")
                        ) ]
                    ),
                ]
            ),
            html.Div(
                className="app-main-card",
                children=[
                    html.Div(
                        className="app-main-card-title",
                        children=[ html.H3("Poblacion del continente Europeo") ],
                        style={'background-color': '#00a859'}
                    ),
                    html.Div(
                        className="app-main-card-body",
                        children=[ dcc.Graph(
                            figure=
                            px.pie(
                                px.data.gapminder().query("year == 2007").query("continent == 'Europe'"),
                                values='pop',
                                names='country',
                            )
                        ) ]
                    ),
                ]
            ),
        ]
    ),




    html.Div(
        className="app-vento",
        children=[
            html.Div(
                className="app-vento-card c1",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figBarras )]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card c2",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figCuadro )]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card c3",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figBarras )]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card c4",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figCuadro )]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card m1",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figPie) ]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card m2",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figMapa )]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card m3",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure= figMapa)]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card m4",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure=figPie) ]
                    ),
                ]
            ),
            html.Div(
                className="app-vento-card s1",
                children=[
                    html.Div(
                        className="app-vento-card-title",
                        children=[ html.H3("Experiencia de Vida por Pais") ],
                        style={'background-color': '#4da6d1'}
                    ),
                    html.Div(
                        className="app-vento-card-body",
                        children=[ dcc.Graph( style={'height': '100%', 'width': '100%'},
                                              config={'responsive': True}, figure= figGlobo) ]
                    ),
                ]
            )
        ]
    ),


    html.Div(
        className="app-table",
        children=[
            html.Div(
                className="app-table-title",
                children=[ html.H3("Tabla de ventas") ],
                style={'background-color': '#e65541'}
            ),
            html.Div(
                className="app-table-main",
                children=[
                    dag.AgGrid(
                        rowData = df.to_dict('records'),
                        columnDefs = [ {"field": i} for i in df.columns]
                    )
                ]
            )
        ]
    ),
    html.Div(
        className="app-table",
        children=[
            html.Div(
                className="app-table-title",
                children=[ html.H3("Precio unitario de venta por region") ],
                style={'background-color': '#5c59a7'}
            ),
            html.Div(
                className="app-table-main",
                children=[
                    dcc.RadioItems(options=['Unit Price', 'Unit Cost', 'Units Sold'], value='Units Sold', id='controls-radio-item'),
                    dcc.Graph(figure={}, id='controls-graph')
                ]
            )
        ]
    )
]


@callback(
    Output(component_id='controls-graph', component_property='figure'),
    Input(component_id='controls-radio-item', component_property='value')
)
def update_graph(col_choosen):
    fig = px.histogram(df, x='Region', y=col_choosen, histfunc='avg')
    return fig