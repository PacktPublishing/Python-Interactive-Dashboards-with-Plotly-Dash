from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')


app = Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target='_blank')]),
    dcc.Dropdown(id='country-dropdown',
                 options=happiness['country'].unique(),
                 value='United States'),
    dcc.Graph(id='happiness-graph', figure={})])


@app.callback(
    Output(component_id='happiness-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'))
def update_graph(selected_country):
    filtered_happiness = happiness[happiness['country'] == selected_country]
    line_fig = px.line(filtered_happiness,
                       x='year', y='happiness_score',
                       title=f'Happiness Score in {selected_country}')
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)
