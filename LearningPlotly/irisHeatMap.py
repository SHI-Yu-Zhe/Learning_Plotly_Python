import plotly.express as px
iris = px.data.iris()
fig = px.density_heatmap(
    iris,
    x="sepal_width",
    y="sepal_length",
    marginal_x="histogram",
    marginal_y="violin"
)
fig.show()