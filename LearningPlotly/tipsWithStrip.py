import plotly.express as px
tips = px.data.tips()
fig = px.strip(
    tips,
    x="total_bill",
    y="time",
    orientation="v",
    color="smoker"
)
fig.show()
