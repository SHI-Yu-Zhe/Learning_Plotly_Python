import plotly.express as px
iris = px.data.iris()
iris["e"]=iris["sepal_width"]/100
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    error_x="e",
    error_y="e"
)
fig.show()
