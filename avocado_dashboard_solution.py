# Step 1: Exploring the dataset
# The columns that will be used are: date, average_price, type, and geography


# Step 2: Preparing to build the Dash app
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

avocado = pd.read_csv('avocado.csv')

app = Dash()


# Step 3: Building the layout
geo_dropdown = dcc.Dropdown(options=avocado['geography'].unique(),
                            value='New York')

app.layout = html.Div(children=[
    html.H1(children='Avocado Prices Dashboard'),
    geo_dropdown,
    dcc.Graph(id='price-graph')
])


# Step 4: Adding the callback function
@app.callback(
    Output(component_id='price-graph', component_property='figure'),
    Input(component_id=geo_dropdown, component_property='value')
)
def update_graph(selected_geography):
    filtered_avocado = avocado[avocado['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado,
                       x='date', y='average_price',
                       color='type',
                       title=f'Avocado Prices in {selected_geography}')
    return line_fig


# Step 5: Running the dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
