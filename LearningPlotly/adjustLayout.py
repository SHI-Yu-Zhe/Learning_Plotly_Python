import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="sex",
    width=1000,
    height=500
    # adjust the size of figure
)
fig.update_layout(
    margin=dict(l=20,r=20,t=20,b=20),
    # set margin of left,right,top,bottom
    paper_bgcolor="LightSteelBlue"
)
fig.show(
    config={
        'scrollZoom':True,
        'editable':True
    }
)
