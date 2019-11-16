import plotly.graph_objs as go
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species"
)
reference_line = go.Scatter(
    x=[2,4],
    y=[4,8],
    mode="lines",
    line=go.scatter.Line(color="gray"),
    showlegend=False
)
for i in range(1,4):
    fig.add_trace(reference_line,row=1,col=i)
fig.show()
