import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species"
)
fig.update_xaxes(showgrid=False)
fig.show()
