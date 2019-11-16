import plotly.graph_objects as go
fig = go.Figure({
    "data":{
        "type":"scatter",
        "x":[2,5,4,7,3],
        "y":[1,7,4,3,6]
    },
    "layout":{"title":{"text":"test"},}
})
fig.show()
