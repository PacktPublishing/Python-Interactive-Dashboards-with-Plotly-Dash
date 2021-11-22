import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

electricity = pd.read_csv('electricity.csv')

year_min = electricity['Year'].min()
year_max = electricity['Year'].max()

app = dash.Dash()

app.layout = html.Div([
    html.H1('Electricity Prices by US State'),
    dcc.RangeSlider(id='year-slider',
                    min=year_min,
                    max=year_max,
                    value=[year_min, year_max],
                    marks={i: str(i) for i in range(
                        year_min, year_max+1)}
                    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
