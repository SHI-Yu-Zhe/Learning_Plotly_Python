import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species",
    trendline="ols"
)
fig.update_traces(
    line=dict(dash="dot",width=4),
    selector=dict(type="scatter",mode="lines")
)
fig.show()
