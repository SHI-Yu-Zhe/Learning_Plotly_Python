import plotly.graph_objects as go
from plotly.subplots import make_subplots
fig = make_subplots(rows=1,cols=2)
fig.add_trace(go.Scatter(y=[1,5,2],x=[1,2,3],mode="lines"),row=1,col=1)
fig.add_trace(go.Bar(y=[1,2,4],x=[1,2,3]),row=1,col=2)
fig.show()