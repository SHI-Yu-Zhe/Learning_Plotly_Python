import plotly.graph_objs as go
import numpy as np
import os
N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=x,
        y=y,
        mode="markers"
    )
)
if not os.path.exists("images"):
    os.mkdir("images")
fig.write_image("images/f1.jpg")