import plotly.graph_objects as go
fig = go.Figure(
    data=[go.Bar(x=[1,2,3],y=[4,2,5])],
    layout=dict(title=dict(text="bar chart"))
)
fig.show()
