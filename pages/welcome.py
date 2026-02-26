import dash
from dash import html
import dash_bootstrap_components as dbc
from .sidebar import sidebar

dash.register_page( __name__, path='/inicio' )

layout = html.Div([
    html.Div(
        className="app-header-bar",
        children = [
            html.H1("Data analytics dashboard"),
            dbc.Row(
                [dbc.Col(sidebar(), width=2)]
            )
        ],
    ),
])