import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

player_name_options = [{'label': i, 'value': i} for i in soccer[
    'long_name'].unique()]

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    dbc.Row([
        dbc.Col(
            html.P(['Source: ',
                    html.A('Sofifa',
                           href='https://sofifa.com/',
                           target="_blank")
                    ])
        ),
        dbc.Col([
            html.Label('Player name: '),
            dcc.Dropdown(
                options=player_name_options,
                value=player_name_options[0]['value'])
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
