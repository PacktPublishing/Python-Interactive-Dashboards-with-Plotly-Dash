Context


You've learned all the basics for making dashboards using Dash! It's time to test your knowledge.

In this exercise, you'll build an interactive dashboard with a dropdown menu, a figure, plus a callback function to connect them together. The users can interact with the dashboard by changing the option in the dropdown menu and seeing an updated figure.

We'll be using the avocado dataset from Kaggle (download from Resources).



Two ways to complete the exercise


- Build the dashboard without any hints by looking at the final dashboard (https://python-dash-tutorial-example.herokuapp.com/)

- Follow the below instructions and build it step-by-step. Please try to write the code by yourself before looking at the solution.



Instructions


Step 1: Exploring the dataset

- Open the avocado.csv file

Suppose we want to present the average prices of different types of avocados for various geographies across time. What are the columns in the dataset we'll be using?

It's also better to explore the dataset in Jupyter Notebook before building the dashboard. This is optional for this exercise. But if you'd like, please check out our notebook (avocado.ipynb).



Step 2: Preparing to build the Dash app

- Go to an editor like PyCharm and create a new Python file

- Import the libraries

Hint: libraries are needed for loading the dataset, building core, html components, plotly figures, as well as callback functions

- Read the csv file as a pandas DataFrame called avocado

Hint: save the Python script and the dataset avocado.csv in the same directory to avoid setting the path in the read_csv function

- Create a Dash app object called app



Step 3: Building the layout

- Use the keyword layout of the app to specify its layout

- Put three components into the layout:

  - H1 heading with text ‘Avocado Prices Dashboard’

  - A Dropdown with properties:

    - id as 'geo-dropdown', or you can assign the component as a variable 'geo_dropdown'

    - options as the unique values based on column geography

    - value as ‘New York’

  - A Graph component with id ‘price-graph’

Hints:

- Don't forget to use the Div container to hold all three components as a list

- Use the two modules: dash_html_components (html) and dash_core_components (dcc) to build components, for example, html.Div

- Pay attention to the capitalization of the letters in these components



Step 4: Adding the callback function

- Write the decorator section of the callback function

  - start with @app.callback

  - specify the Output and the Input objects by defining their ids and properties

    - the output is the figure property of the graph component

    - the input is the value property of the dropdown component

Hint: to define the Input object, use syntax Input('component_id', 'component_property')

- Define the function below the decorator

  - Start with the keyword def

  - Give it a function name update_graph

  - Call its input parameter selected_geography

  - Generate a filtered dataset called filtered_avocado when geography is selected_geography

  - Create a plotly line figure called line_fig based on this filtered dataset. This figure shows the average prices of different types of avocados across time. Also, give it the title of Avocado Prices in selected_geography.

  - Return the line_fig as the output

Hints:

- The callback function has the same syntax as a regular Python function

- Use the plotly.express (px) to generate the line figure. Besides the dataset, we need to specify its arguments x, y, color, and title

- Use an f-string to make the title of the figure depending on a variable



Step 5: Running the dashboard

- Add the code to run the server with debug being True

- Run the script and take a look

Hint: check whether __name__ == '__main__' before using the run_server method



Please check out the solution in avocado_dashboard_solution.py.