import plotly.express as px

figCuadro = px.treemap(
    px.data.gapminder().query("year == 2007"),
    path=[px.Constant('world'), 'continent', 'country'],
    values='pop',
    color='lifeExp',
    hover_data=['iso_alpha']
)

figCuadro.update_layout(
    autosize=True, 
    font_color="white", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    margin=dict(l=10, r=10, t=35, b=10) 
)
