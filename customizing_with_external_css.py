from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')


app = Dash(external_stylesheets=[dbc.themes.CYBORG])

app.layout = html.Div([
    html.H1('Soccer Players Dashboard'),
    html.P(['Source: ',
            html.A('Sofifa',
                   href='https://sofifa.com/',
                   target='_blank')]),
    html.Label('Player name: '),
    dcc.Dropdown(
        options=soccer['long_name'].unique(),
        value=soccer['long_name'].unique()[0])
])

if __name__ == '__main__':
    app.run_server(debug=True)
