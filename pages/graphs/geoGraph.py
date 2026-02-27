import plotly.express as px

figMapa = px.scatter_geo(
    px.data.gapminder(),
    locations="iso_alpha",
    color="continent",
    hover_name="country",
    size="pop",
    animation_frame="year",
    projection="natural earth"
)

figMapa.update_layout(
    autosize=True, 
    font_color="white", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    margin=dict(l=0, r=0, t=0, b=0), 
    height=500, 
)

figMapa.update_geos( 
    bgcolor='rgba(0,0,0,0)', 
    showframe=False, 
    showcoastlines=True, 
    projection_type="natural earth", 
    coastlinecolor="rgba(255,255,255,0.2)", 
    visible=True, 
    resolution=50, 
    projection_scale=1.2
)
