import plotly.express as px
tips = px.data.tips()
fig = px.histogram(
    tips,
    x="total_bill",
    y="tip",
    color="sex",
    marginal="box",
    hover_data=tips.columns
)
fig.show()
