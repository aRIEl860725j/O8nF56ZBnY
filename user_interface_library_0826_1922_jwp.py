# 代码生成时间: 2025-08-26 19:22:55
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

# Define the main application layout
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    # Define a header
    html.H1('User Interface Component Library'),
    # Define a dropdown for selecting a component
    dcc.Dropdown(
        id='component-dropdown',
        options=[
            {'label': 'Graph', 'value': 'graph'},
            {'label': 'Table', 'value': 'table'},
            {'label': 'Slider', 'value': 'slider'},
        ],
        value='graph',
    ),
    # Define a placeholder for the component layout
    html.Div(id='component-layout', children=[]),
])

# Define a callback function to update the component layout based on the selection
@app.callback(
    Output('component-layout', 'children'),
    Input('component-dropdown', 'value')
)
def update_component_layout(selected_component):
    # Check if the selected component is 'graph'
    if selected_component == 'graph':
        # Return a graph component layout
        return dcc.Graph(figure={'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]}]})
    # Check if the selected component is 'table'
    elif selected_component == 'table':
        # Load sample data for the table
        sample_data = pd.DataFrame({'Name': ['John', 'Mary', 'David'], 'Age': [28, 34, 29]})
        # Return a table component layout
        return dash_table.DataTable(
            columns=[{'name': i, 'id': i} for i in sample_data.columns],
            data=sample_data.to_dict('records')
        )
    # Check if the selected component is 'slider'
    elif selected_component == 'slider':
        # Return a slider component layout
        return dcc.Slider(
            id='example-slider',
            min=0,
            max=20,
            value=10,
            marks={i: f'{i}' for i in range(0, 21, 2)},
            step=1
        )
    else:
        # Raise a PreventUpdate exception if the selected component is not valid
        raise PreventUpdate

# Define the run server command and address
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
