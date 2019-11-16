import plotly.express as px
iris = px.data.iris()
fig = px.parallel_coordinates(
    iris,
    color="species_id",
    labels={
        "species_id":"species",
        "sepal_width":"Sepal Width",
        "sepal_length":"Sepal Length",
        "petal_width":"Petal Width",
        "petal_length":"Petal Length"
    },
    color_continuous_scale=px.colors.diverging.Tealrose,
    color_continuous_midpoint=2
)
fig.show()
