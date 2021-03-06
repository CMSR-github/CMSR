import dash
import dash_core_components as dcc
from dash.dependencies import Output
from dash.dependencies import Input
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from BatteryManagement import BatteryManagement
import os


X = deque(maxlen = 20)
X.append(0)
Y = deque(maxlen = 20)

BMS = BatteryManagement()

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Img(src=app.get_asset_url("Scotty Boat Transparent.png"),
                 alt="failure",
                 height=100),
        dcc.Graph(id='live-graph', animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 1000
        )
    ]
)

@app.callback (Output('live-graph','figure'), 
                [Input('graph-update','n_intervals')]) 

def update_graph(n):
    global X
    global Y
    BSoC = BMS.get_BSoC()

    X.append(X[-1]+1)
    #X[-1]+Y[-1]*random.uniform(-0.1,0.1)
    Y.append(BSoC)

    data = go.Scatter(
        x = list(X),
        y = list(Y),
        name = 'Scatter',
        mode = 'lines+markers'
    )

    return {'data':[data],'layout': go.Layout(xaxis = dict(range=[min(X),max(X)]),
                                            yaxis = dict(range=[0,100]))}

if __name__ == '__main__':
    app.run_server(debug = True)
