import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate

life_expectancy = pd.read_csv('life_expectancy.csv')

navbar = dbc.NavbarSimple(
    brand='Life Expectancy Dashboard',
    brand_style={'fontSize': 40, 'color': 'white'},
    children=html.A('Data Source',
               href='https://ourworldindata.org/life-expectancy',
               target='_blank',
               style={'color': 'black'}),
    color='primary',
    fluid=True,
    sticky='top'
)

year_min = life_expectancy['year'].min()
year_max = life_expectancy['year'].max()

year_slider = dcc.RangeSlider(
        id='year-slider',
        min=year_min,
        max=year_max,
        value=[year_min, year_max],
        marks={i: str(i) for i in range(year_min, year_max+1, 10)}
    )

input_card = dbc.Card(
    dbc.CardBody([
        html.H5('Life expectancy by countries'),
        year_slider,
        html.Div(id='year-text')
    ]),
    style={'textAlign': 'center', 'color': 'white'},
    color='darkblue'
)

country_options = [{'label': i, 'value': i} for i in life_expectancy[
    'country'].unique()]

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    navbar,
    input_card,
    html.Br(),
    dcc.Dropdown(id='country-dropdown',
                 options=country_options,
                 multi=True),
    html.Br(),
    html.Button(id='submit-button',
                children='Submit'),
    html.Br(),
    dcc.Graph(id='life-expectancy-graph'),
])

@app.callback(
    Output('year-text', 'children'),
    Input('year-slider', 'value'))
def update_year(selected_years):
    return f'Selected years: {selected_years[0]} - {selected_years[1]}'


@app.callback(
    Output('life-expectancy-graph', 'figure'),
    Input('submit-button', 'n_clicks'),
    State('country-dropdown', 'value'),
    State('year-slider', 'value'))
def update_outputs(button_click, selected_country, selected_years):
    if selected_country is None:
       raise PreventUpdate
    msk = (life_expectancy['country'].isin(selected_country)) & \
          (life_expectancy['year'] >= selected_years[0]) & \
          (life_expectancy['year'] <= selected_years[1])
    life_expectancy_filtered = life_expectancy[msk]
    line_fig = px.line(life_expectancy_filtered,
                       x='year', y='life expectancy',
                       title='Life expectancy',
                       color='country')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)