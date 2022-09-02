from dash import Dash, html, dcc, Input, Output

app = Dash()

app.layout = html.Div([
    dcc.Input(id='input-text', value='Change this text', type='text'),
    html.Div(children='', id='output-text')
                       ])


@app.callback(
    Output(component_id='output-text', component_property='children'),
    Input(component_id='input-text', component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'


if __name__ == '__main__':
    app.run_server(debug=True)
