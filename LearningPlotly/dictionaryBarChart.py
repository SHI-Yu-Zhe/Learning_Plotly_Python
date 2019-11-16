import plotly.io as pio

fig = {
    "data":[{
        # nested dictionary
        "type":"bar",
        "x":[2011,2012,2013,2014],
        "y":[32,54,21,42]
    }],
    "layout":{"title":{"text":"bar chart"}}
}

pio.show(fig)
