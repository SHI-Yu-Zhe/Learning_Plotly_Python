import plotly.express as px
gapminder=px.data.gapminder()
gapminder_2007=gapminder.query("year==2007")

for template in ["plotly_dark","xgridoff","presentation","ggplot2"]:
    fig = px.scatter(
        gapminder_2007,
        x="gdpPercap",
        y="lifeExp",
        size="pop",
        color="continent",
        log_x=True,
        size_max=60,
        template=template,
        title="Gapminder 2007:'%s' theme" % template
    )
    fig.show()

