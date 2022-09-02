from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

electricity = pd.read_csv('electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

avg_price_electricity = electricity.groupby('US_State')['Residential Price'].mean().reset_index()
map_fig = px.choropleth(avg_price_electricity,
                        locations='US_State', locationmode='USA-states',
                        color='Residential Price', scope='usa',
                        color_continuous_scale='reds')


app = Dash()

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(
                        year_min, year_max+1)}
                    ),
    dcc.Graph(id='map-graph', figure=map_fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
