import plotly.express as px
wind = px.data.wind()
fig = px.line_polar(
    wind,
    r="frequency",
    theta="direction",
    line_close=True,
    color="strength",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()
