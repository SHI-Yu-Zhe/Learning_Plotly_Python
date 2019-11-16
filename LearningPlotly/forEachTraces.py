import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species"
)
fig.for_each_trace(
    lambda trace:trace.update(name=trace.name.replace("=",":"))
)
fig.show()
