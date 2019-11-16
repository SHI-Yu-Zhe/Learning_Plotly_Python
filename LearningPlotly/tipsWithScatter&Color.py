import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="sex",
    color_continuous_scale=px.colors.sequential.Viridis,
    color="size",
    render_mode="webg1"
)
fig.show()
