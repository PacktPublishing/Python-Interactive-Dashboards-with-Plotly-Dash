from dash import Dash, html

app = Dash()

app.layout = html.Div('My Dashboard')

if __name__ == '__main__':
    app.run_server(debug=True)
