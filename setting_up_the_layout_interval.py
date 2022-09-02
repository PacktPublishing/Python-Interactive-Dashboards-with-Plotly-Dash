from dash import Dash, html, dcc, dash_table
import plotly.graph_objects as go
import yfinance as yf

app = Dash()


price = yf.Ticker('AAPL').history(period='1d', interval='15m').reset_index()

fig = go.Figure(data=go.Candlestick(
                        x=price['Datetime'],
                        open=price['Open'],
                        high=price['High'],
                        low=price['Low'],
                        close=price['Close']))

app.layout = html.Div([
    html.H1('My financial dashboard'),
    dcc.Input(id='ticker-input',
              placeholder='Search for symbols from Yahoo Finance',
              style={'width': '50%'}),
    html.Button(id='submit-button', children='Submit'),
    html.Br(),
    html.Br(),
    dcc.Tabs([
        dcc.Tab(label='Candlestick Chart',
                children=dcc.Graph(id='stock-graph',
                                   figure=fig)),
        dcc.Tab(label='Recent Data',
                children=dash_table.DataTable(id='stock-data',
                                              data=price.tail(10).to_dict('records')))
            ]),
    dcc.Interval(id='chart-interval', interval=1000*60*15, n_intervals=0),
    dcc.Interval(id='table-interval', interval=1000*60, n_intervals=0)
])


if __name__ == '__main__':
    app.run_server(debug=True)
