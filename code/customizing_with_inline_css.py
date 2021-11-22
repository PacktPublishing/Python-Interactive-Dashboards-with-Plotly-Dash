import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

player_name_options = [{'label': i, 'value': i} for i in soccer[
    'long_name'].unique()]

app = dash.Dash()

app.layout = html.Div([
    html.H1('Soccer Players Dashboard',
            style={'textAlign': 'center',
                   'fontFamily': 'fantasy',
                   'fontSize': 50,
                   'color': 'blue'}),
    html.P(['Source: ',
            html.A('Sofifa',
                   href='https://sofifa.com/',
                   target="_blank")],
           style={'border': 'solid'}),
    html.Label('Player name: '),
    dcc.Dropdown(
        options=player_name_options, value=player_name_options[0][
            'value'],
        style={'backgroundColor': 'lightblue'})],
    style={'padding': 100, 'border': 'solid'})

if __name__ == '__main__':
    app.run_server(debug=True)
