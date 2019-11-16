import plotly.express as px
tips = px.data.tips()
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    facet_col="day",
    facet_row="time",
    color="smoker",
    category_orders={
        "day":["Thur","Fri","Sat","Sun"],
        "time":["Lunch","Dinner"]
    }
)
fig.show()
