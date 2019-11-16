import plotly.graph_objs as go
import pandas as pd
z_data = pd.read_csv("mt_bruno_elevation.csv")
fig = go.Figure(
    data=go.Surface(z=z_data.values),
    layout=go.Layout(
        title="Mt Bruno Elevation",
        width=500,
        height=500
    )
)
for template in ["plotly","plotly_dark","ggplot2","seaborn"]:
    fig.update_layout(
        template=template,
        title="Mt Bruno Elevation:'%s' theme" % template
    )
    fig.show()
