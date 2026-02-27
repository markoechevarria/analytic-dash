import plotly.express as px

dfpie = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")

dfpie.loc[dfpie['pop'] < 3.e6, 'country'] = 'Other countries'

figPie = px.pie(
    dfpie,
    values='pop',
    names='country',
)

figPie.update_layout(
    autosize=True,  
    font_color="white", 
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)', 
    margin=dict(l=10, r=10, t=35, b=10) 
)
