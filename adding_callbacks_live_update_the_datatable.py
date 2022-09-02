from dash import Dash, html, dcc, dash_table, Input, Output, State
import plotly.graph_objects as go
import yfinance as yf

app = Dash()


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
                children=dcc.Graph(id='stock-graph')),
        dcc.Tab(label='Recent Data',
                children=[html.Div(id='latest-price-div'),
                          dash_table.DataTable(id='stock-data')])
    ]),
    dcc.Interval(id='chart-interval', interval=1000*60*15, n_intervals=0),
    dcc.Interval(id='table-interval', interval=1000*60, n_intervals=0)
])


@app.callback(Output('stock-graph', 'figure'),
              Input('submit-button', 'n_clicks'),
              Input('chart-interval', 'n_intervals'),
              State('ticker-input', 'value'))
def update_chart(button_click, chart_interval, ticker):
    if ticker is None:
        return {}
    else:
        price = yf.Ticker(ticker).history(period='1d', interval='15m').reset_index()
        if len(price) > 0:
            fig = go.Figure(data=go.Candlestick(
                            x=price['Datetime'],
                            open=price['Open'],
                            high=price['High'],
                            low=price['Low'],
                            close=price['Close']))
            return fig
        else:
            return {}


@app.callback(Output('latest-price-div', 'children'),
              Output('stock-data', 'data'),
              Input('submit-button', 'n_clicks'),
              Input('table-interval', 'n_intervals'),
              State('ticker-input', 'value'))
def update_table(button_click, table_interval, ticker):
    if ticker is None:
        return '', []
    else:
        price = yf.Ticker(ticker).history(period='1d', interval='1m').reset_index().tail(10)
        if len(price) > 0:
            latest_price = price['Close'].iloc[-1]
            latest_time = price['Datetime'].max().strftime('%b %d %Y %I:%M:%S %p')
            return f'The latest price is {latest_price} at the time of {latest_time}', \
                   price.to_dict('records')
        else:
            return f'No data for ticker {ticker} on Yahoo Finance', []


if __name__ == '__main__':
    app.run_server(debug=True)
