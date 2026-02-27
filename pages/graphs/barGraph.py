import plotly.express as px
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from data.data import df

figBarras = px.histogram(
    df[df["Country"].str.startswith('A')],
    x='Country',
    y='Total Revenue',
    labels={ "Country": "Pais", "Total Revenue": "Ingresos Totales" },
    histfunc='avg'
)

figBarras.update_layout( 
    autosize=True, 
    font_color="white", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    margin=dict(l=10, r=10, t=35, b=10) 
)

figBarras.update_traces(textfont_color="white")