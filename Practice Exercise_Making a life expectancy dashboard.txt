Context


You've learned a lot in this course! So let's practice the key knowledge, and even learn something new in this last exercise.



How did life expectancy change in our world?

You'll build a stylish, interactive dashboard to answer this question. Please check out the final dashboard here. Please explore the dashboard, and use it as a reference throughout the exercise.

You can follow the step-by-step instructions below. To make the practice more realistic and challenging, we didn't list details. Please aim for making the dashboard look roughly the same, and have the same interactive features.



Good luck!



Instructions


Step 1: Exploring the dataset

- Open the life_expectancy.csv file

Suppose we want to compare the changes in life expectancy for different countries across time. What are the columns in the dataset we'll be using?



Step 2: Preparing to build the Dash app

- Import the libraries

Please explore the final dashboard to see the necessary libraries. Yet, you can always add more libraries later.



- Read the csv file as a pandas DataFrame



- Create a Dash object called app, link to the standard Bootstrap stylesheet



Step 3: Building the layout

- Put the following components into the layout:

  - NavbarSimple as shown on the final dashboard:

    - data source: https://ourworldindata.org/life-expectancy

    - sticky on top

Hint: in the course, we didn't show how to style the brand text or make the bar sticky. Please research the official doc of NavbarSimple for the solution. This is how you learn to use a new Dash component.



  - A Card to hold:

    - a heading of 'Life expectancy by countries'

    - a year RangeSlider as shown in the final dashboard, with the currently selected range being the entire range. This RangeSlider will be used in a callback function

       - use the tooltip property to display the current value of the RangeSlider

          Hint: please research the official doc for how to use tooltip



  - A line breaker



  - A multi-value Dropdown component, which shows the unique countries. It will be used in a callback function

Hint: we didn't show the multi-value Dropdown in the course. But you can research it in the official doc of the Dropdown component.



  - A line breaker



  - A Button that will be used in a callback function



  - A line breaker



  - A Graph component that will be used in a callback function



We strongly suggest testing out the code to see if the layout looks good, before moving on to the next step.

Again, since we didn't provide all the details, you've completed the layout as long as it looks similar to the final dashboard.



Step 4: Adding callback function

The callback connects the year RangeSlider, country Dropdown, submit Button, and the Graph

Interactive feature: explore by

  - changing the selection of the year RangeSlider

  - select multiple countries in the Dropdown

  - click the submit Button

What happens to the Graph?



Hints:

- Note that the update only happens after the submit Button is clicked.

- Don't forget that the value property of the country Dropdown could have multiple values, so try the isin method when filtering.

- If you didn't set the value property within the country Dropdown, you would get an error message as below:



Callback error updating life-expectancy-graph.figure

TypeError: only list-like objects are allowed to be passed to isin(), you passed a [NoneType]



This is because, without the value property, the country Dropdown's value can be None.

You can use the PreventUpdate command:

   - from dash.exceptions import PreventUpdate

   - add the below code to the beginning of the callback function:

 if selected_country is None:
        raise PreventUpdate
 # selected_country is the input variable name corresponding to the country Dropdown's value property
When nothing is selected in the country Dropdown, selected_country is None, the PreventUpdate command prevents the updating of the output. This will fix the problem.

Alternatively, you can also return an empty figure, as shown in the lessons of Case study II.



Step 5: Testing the dashboard

Run the script and test the interactive features

Again, as long as you have a similar layout and the same interactive features as the final dashboard, you've completed the exercise!



Please check out the solution in life_expectancy_dashboard_solution.py.