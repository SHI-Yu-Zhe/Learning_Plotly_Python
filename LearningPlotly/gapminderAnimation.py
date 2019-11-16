import plotly.express as px
gapminder = px.data.gapminder()
fig = px.scatter(
    gapminder,
    animation_frame="year",
    animation_group="country",
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    facet_col="continent",
    log_x=True,
    size_max=45,
    range_x=[100,100000],
    range_y=[25,90]
)
fig.show()
