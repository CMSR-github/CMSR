import dash
import dash_core_components as dcc
from dash.dependencies import Output
from dash.dependencies import Input
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen = 20)
X.append(1)
Y = deque(maxlen = 20)
Y.append(1)

app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate = True),
        dcc.Interval(
            id = 'graph-update',
            interval = 600
        )              
    ]
)

@app.callback (Output('live-graph','figure'), 
                [Input('graph-update','n_intervals')]) 

def update_graph(n):
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(X[-1]+Y[-1]*random.uniform(-0.1,0.1))

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
