from dash import Dash, html, dcc

app = Dash()


app.layout = html.Div([
    html.H1('My financial dashboard'),
    dcc.Input(id='ticker-input',
              placeholder='Search for symbols from Yahoo Finance',
              style={'width': '50%'}),
    html.Button(id='submit-button', children='Submit')
])


if __name__ == '__main__':
    app.run_server(debug=True)
