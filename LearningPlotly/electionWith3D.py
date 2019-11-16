import plotly.express as px
ele = px.data.election()
fig = px.scatter_3d(
    ele,
    x="Joly",
    y="Coderre",
    z="Bergeron",
    color="winner",
    size="total",
    color_discrete_map={
        "Joly":"blue",
        "Bergeron":"green",
        "Coderre":"red"
    },
    hover_name="district",
    symbol="result"
)
fig.show()
