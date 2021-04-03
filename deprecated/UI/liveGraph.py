#https://pythonprogramming.net/live-graphs-data-visualization-application-dash-python-tutorial/import dash


from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

x = deque(maxlen = 20)
y = deque(maxlen = 20)
X.append(1)
Y.append(1)

app = dash.Dash(__name__)

#triggers an event
#in ms, runs every 1 second
#updating done using javascript, id used to update
app.layout = html.Div(
        [   
        dcc.Graph(id = 'live-graph', animate = True), 
        dcc.Interval(
            id = 'graph-update', 
            interval = 1000 
            )
        ]
    )

#must pass figure in order to display anything
@app.callback(Output('live-graph', 'figure'), 
                events = [Event('graph-update', 'interval')]) 
def update_graph():
    global X
    global Y
    X.append(X[-1] + 1)
    Y.append(Y[-1] + Y[-1]*random.uniform(-0.1, 0.1))

    #scatter plot
    #takes a scatter graph and adds lines
    data = go.scatter( 
    x = list(X),
    y = list(Y),
    name = 'Scatter',
    mode = 'lines+markers' 
    ) 
    #makes it so that the axis updates and increases as values are added
    return {'data':[data], 'layout': go.Layout(xaxis = dict(xaxis = dict(range = [min(X), max(X)]),
                                                yaxis = dict(range = [min(Y), max(Y)])))} 

if __name__ == '__main__':
    app.run_server(debug = True)


