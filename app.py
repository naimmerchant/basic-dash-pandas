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
app.title='Election Results'
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/naimmerchant/basic-dash-pandas/master/NC_PrecinctData.csv")

colors_list=list(df['county_name'].value_counts().index)




####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a category:'),
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
def display_value(user_input):
    df1 = df.loc[df['county_name']==user_input]
    results = df1.groupby('party')['votes'].sum()
    mydata = [go.Bar(x = results.index,
                 y = results.values,
                 marker = dict(color='blue'))]
    mylayout = go.Layout(title = 'Election Results',
                     xaxis = dict(title='Category'),
                     yaxis = dict(title='Total Votes'))
    myfig = go.Figure(data=mydata, layout=mylayout)
    return myfig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
