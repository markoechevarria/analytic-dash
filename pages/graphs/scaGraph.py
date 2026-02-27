import plotly.express as px

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

figGlobo.update_layout(
    autosize=True, 
    font_color="white", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    margin=dict(l=0, r=0, t=0, b=0), 
    height=500, 
)