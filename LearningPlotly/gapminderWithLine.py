import plotly.express as px
gapminder = px.data.gapminder()
fig = px.line(
    gapminder,
    x="year",
    y="lifeExp",
    color="continent",
    line_group="country",
    hover_name="country",
    line_shape="spline",
    render_mode="svg"
)
fig.show()
