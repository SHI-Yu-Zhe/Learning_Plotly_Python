import plotly.express as px
ele = px.data.election()
fig = px.scatter_ternary(
    ele,
    a="Joly",
    b="Coderre",
    c="Bergeron",
    color="winner",
    size="total",
    hover_name="district",
    color_discrete_map={
        "Joly":"blue",
        "Bergeron":"green",
        "Coderre":"red",
    },
    size_max=15
)
fig.show()
