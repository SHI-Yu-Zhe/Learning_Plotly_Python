import plotly.express as px
wind = px.data.wind()
fig = px.scatter_polar(
    wind,
    r="frequency",
    theta="direction",
    symbol="strength",
    color="strength",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()
