import plotly.express as px
wind = px.data.wind()
fig = px.bar_polar(
    wind,
    r="frequency",
    theta="direction",
    color="strength",
    template="plotly_dark",
    color_discrete_sequence=px.colors.sequential.Plasma[-2::-1]
)
fig.show()
