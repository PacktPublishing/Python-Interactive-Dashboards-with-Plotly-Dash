import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

soccer = pd.read_csv('fifa_soccer_players.csv')

avg_age = soccer['age'].mean()
avg_height = soccer['height_cm'].mean()
avg_weight = soccer['weight_kg'].mean()
sofifa_logo = "https://uptime.com/media/website_profiles/sofifa.com.png"

navbar = dbc.NavbarSimple(
    brand='Soccer Players Dashboard',
    children=[
        html.Img(src=sofifa_logo, height=20),
        html.A('Data Source',
               href='https://sofifa.com/',
               target='_blank',
               style={'color': 'black'})
            ],
    color='primary',
    fluid=True
)

cards = dbc.CardDeck([
            dbc.Card(
                dbc.CardBody([
                        html.H4('Avg. Age'),
                        html.H5(f'{round(avg_age, 1)} years')
                    ])
                ,
                style={'textAlign': 'center', 'color': 'white'},
                color='lightblue'
            ),
            dbc.Card(
                dbc.CardBody([
                        html.H4('Avg. Height'),
                        html.H5(f'{round(avg_height, 1)} cm')
                    ])
                ,
                style={'textAlign': 'center', 'color': 'white'},
                color='blue'
            ),
            dbc.Card(
                dbc.CardBody([
                        html.H4('Avg. Weight'),
                        html.H5(f'{round(avg_weight, 1)} kg')
                    ]
                ),
                style={'textAlign': 'center', 'color': 'white'},
                color='darkblue'
            )
    ])

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([navbar, html.Br(), cards])

if __name__ == '__main__':
    app.run_server(debug=True)
