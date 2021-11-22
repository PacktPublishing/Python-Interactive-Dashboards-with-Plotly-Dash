import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

region_options = [{'label': i, 'value': i} for i in happiness[
    'region'].unique()]
data_options = [{'label': 'Happiness Score', 'value': 'happiness_score'},
                {'label': 'Happiness Rank', 'value': 'happiness_rank'}]


app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    dcc.RadioItems(id='region-radio',
                   options=region_options,
                   value='North America'),
    dcc.Dropdown(id='country-dropdown',
                 options=[],
                 value=''),
    dcc.RadioItems(id='data-radio',
                   options=data_options,
                   value='happiness_score'),
    html.Br(),
    html.Button(id='submit-button-state',
                n_clicks=0,
                children='Update the Output'),

    dcc.Graph(id='happiness-graph'),
    html.Div(id='average-div')])


@app.callback(
    Output('country-dropdown', 'options'),
    Output('country-dropdown', 'value'),
    Input('region-radio', 'value'))
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region'] == selected_region]
    country_options = [{'label': i, 'value': i} for i in
                       filtered_happiness['country'].unique()]
    return country_options, country_options[0]['value']


@app.callback(
    Output('happiness-graph', 'figure'),
    Output('average-div', 'children'),
    Input('submit-button-state', 'n_clicks'),
    State('country-dropdown', 'value'),
    State('data-radio', 'value'))
def update_graph(button_click, selected_country, selected_data):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x="year", y=selected_data,
                       title=f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_data} for {selected_country} is {selected_avg}'


if __name__ == '__main__':
    app.run_server(debug=True)
