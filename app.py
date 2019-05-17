######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


####### Set up your app #####
app = dash.Dash(__name__)
server = app.server
app.title='Whatever I want!'
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/00%20resources/titanic.csv")
results = df.groupby('Sex')['Age'].mean()
colors_list=['blue', 'green', 'orange', 'red', 'yellow']




####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a color from the list:'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in colors_list],
        value=colors_list[0]
    ),
    html.Br(),
    dcc.Graph(id='display-value')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('display-value', 'figure'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(color_you_chose):
    mydata = [go.Bar(x = results.index,
                     y = results.values,
                     marker = dict(color=color_you_chose))]
    mylayout = go.Layout(title = 'This is a cool bar chart',
                         xaxis = dict(title='this is my x-axis'),
                         yaxis = dict(title='this is my y-axis'))
    myfig = go.Figure(data=mydata, layout=mylayout)
    return myfig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
