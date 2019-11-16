import plotly.express as px
gapminder = px.data.gapminder()
g_2007 = gapminder.query("year==2007")
fig = px.scatter(
    g_2007,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60
)
fig.show()
