import plotly.graph_objs as go
fig = go.Figure(data=go.Bar(x=[1,2,3],y=[2,5,3]))
fig.data[0].marker.line.width=4
fig.data[0].marker.line.color="black"
fig.show()