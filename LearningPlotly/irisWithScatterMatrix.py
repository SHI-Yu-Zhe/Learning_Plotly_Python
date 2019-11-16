import plotly.express as px
iris = px.data.iris()
fig = px.scatter_matrix(
    iris,
    color="species",
    dimensions=["sepal_width","sepal_length","petal_width","petal_length"]
)
fig.show()