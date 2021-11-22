import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_table
import plotly.express as px
import pandas as pd

electricity = pd.read_csv('electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(
                        year_min, year_max+1)}
                    ),
    dcc.Graph(id='map-graph'),
    dash_table.DataTable(
        id='price-info',
        columns=[{'name': col, 'id': col} for col in electricity.columns],
        data=electricity.to_dict('records')
    )
])


@app.callback(
    Output('map-graph', 'figure'),
    Input('year-slider', 'value'))
def update_map_graph(selected_years):
    filtered_electricity = electricity[(
        electricity['Year'] >= selected_years[0]) & (electricity['Year'] <= selected_years[1])]
    avg_price_electricity = filtered_electricity.groupby('US_State')['Residential Price'].mean().reset_index()
    map_fig = px.choropleth(avg_price_electricity,
                            locations='US_State', locationmode='USA-states',
                            color='Residential Price', scope='usa',
                            color_continuous_scale='reds')
    return map_fig


if __name__ == '__main__':
    app.run_server(debug=True)
