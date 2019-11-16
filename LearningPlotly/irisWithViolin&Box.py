import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_x="box",
    marginal_y="violin"
)
fig.show()
