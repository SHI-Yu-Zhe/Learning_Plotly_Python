import plotly.express as px
iris = px.data.iris()
(px.scatter(
    iris,
    x="sepal_width",
    y="sepal_length",
    color="species",
    facet_col="species",
    title="Iris Dataset"
).update_layout(title_font_size=32)
 .update_yaxes(showgrid=False)
 .update_traces(
    line=dict(dash="dot",width=4),
    selector=dict(type="scatter",mode="lines")
)).show()