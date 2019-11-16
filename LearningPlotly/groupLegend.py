import plotly.graph_objs as go
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[2,1,3],
    legendgroup="group1",
    name="first legend group",
    mode="markers",
    marker=dict(color="crimson",size=15)
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[1,1,1],
    legendgroup="group1",
    name="first legend group",
    mode="lines",
    line=dict(color="crimson")
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[4,7,5],
    legendgroup="group2",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple",size=15)
))
fig.add_trace(go.Scatter(
    x=[1,2,3],
    y=[6,6,6],
    legendgroup="group2",
    name="second legend group",
    mode="lines",
    line=dict(color="MediumPurple")
))
fig.show()
