import plotly.graph_objs as go
fig1 = go.Figure(
    data=[go.Scatter(y=[1,3,2],x=[1,2,3],line=dict(color="crimson"))],
    layout=dict(title=dict(text="chart"))
)
fig1.show()
fig2 = go.Figure(data=go.Bar(y=[1,3,2]))
fig2.update_layout(
    title_text="chart",
    title_font_size=30
)
fig2.show()

