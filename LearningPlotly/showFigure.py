import plotly.io as pio
pio.renderers.default="browser"
import plotly.graph_objects as go
fig = go.Figure(
    data = [go.Bar(y=[2,5,3,1,7,3])],
    layout_title_text = "show figure"
)
fig.show()
