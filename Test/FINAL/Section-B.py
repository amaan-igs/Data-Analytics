import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# data
data = {
    "Flower": ["Rose", "Sunflower", "Tulip", "Lily", "Daisy", "Orchid", "Marigold"],
    "Color": ["Red", "Yellow", "Pink", "White", "Blue", "Purple", "Orange"],
    "Count": [30, 15, 10, 8, 5, 12, 18]
}

df = pd.DataFrame(data)

bar_fig = px.bar(df, x="Flower", y="Count", color="Color",
                 title="Number of Flowers in the Garden",
                 labels={"Count": "Number of Flowers"},
                 color_discrete_map={"Red": "red", "Yellow": "yellow", "Pink": "pink", "White": "white", "Blue": "blue", "Purple": "purple", "Orange": "orange"})

pie_fig = px.pie(df, names="Flower", values="Count",
                 title="Flower Distribution in the Garden")

app.layout = html.Div(children=[
    html.H1(children="Garden Flower Dashboard"),
    
    html.Div(children="Amaan Ul Haq Siddiqui"),
    
    # bar chart
    dcc.Graph(
        id='bar-chart',
        figure=bar_fig
    ),
    
    # pie chart
    dcc.Graph(
        id='pie-chart',
        figure=pie_fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)

# Amaan Ul Haq Siddiqui NAVTTC-BDA-IBA
# https://www.linkedin.com/in/amaanulhaqsiddiqui/