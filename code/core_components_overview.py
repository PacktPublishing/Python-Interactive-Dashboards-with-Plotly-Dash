import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

region_options = [{'label': i, 'value': i} for i in happiness[
    'region'].unique()]
country_options = [{'label': i, 'value': i} for i in happiness[
    'country'].unique()]
line_fig = px.line(happiness[happiness['country'] == 'United States'],
                   x="year", y="happiness_score",
                   title='Happiness Score in the USA')

app = dash.Dash()

app.layout = html.Div([
    html.H1('World Happiness Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='https://worldhappiness.report/',
                   target="_blank")]),
    dcc.RadioItems(options=region_options, value='North America'),
    dcc.Checklist(options=region_options, value=['North America']),
    dcc.Dropdown(options=country_options, value='United States'),
    dcc.Graph(figure=line_fig)])

if __name__ == '__main__':
    app.run_server(debug=True)