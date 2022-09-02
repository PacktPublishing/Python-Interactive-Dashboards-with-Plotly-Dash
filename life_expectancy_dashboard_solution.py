from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
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
        min=year_min,
        max=year_max,
        value=[year_min, year_max],
        marks={i: str(i) for i in range(year_min, year_max+1, 10)},
        step=1,
        tooltip={'placement': 'top', 'always_visible': True}
    )

input_card = dbc.Card([
        html.H5('Life expectancy by countries'),
        year_slider
    ],
    body=True,
    style={'textAlign': 'center', 'color': 'white'},
    color='darkblue'
)


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div([
    navbar,
    input_card,
    html.Br(),
    dcc.Dropdown(id='country-dropdown',
                 options=life_expectancy['country'].unique(),
                 multi=True),
    html.Br(),
    html.Button(id='submit-button',
                children='Submit'),
    html.Br(),
    dcc.Graph(id='life-expectancy-graph'),
])


@app.callback(
    Output('life-expectancy-graph', 'figure'),
    Input('submit-button', 'n_clicks'),
    State('country-dropdown', 'value'),
    State(year_slider, 'value'))
def update_output(button_click, selected_country, selected_years):
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
