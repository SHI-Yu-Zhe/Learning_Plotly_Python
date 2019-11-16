import plotly.express as px
tips = px.data.tips()
fig = px.parallel_coordinates(
    tips,
    color="size",
    color_continuous_scale=px.colors.sequential.Inferno
)
fig.show()
