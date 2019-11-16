import plotly.express as px
gapminder = px.data.gapminder()
fig = px.area(
    gapminder,
    x="year",
    y="pop",
    color="continent",
    line_group="country",
    hover_name="country"
)
fig.show()
