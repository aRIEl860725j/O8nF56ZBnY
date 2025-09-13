# 代码生成时间: 2025-09-13 09:01:58
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import numpy as np

# Define the app layout
def app_layout():
    app = dash.Dash(__name__)
    app.layout = html.Div(
        children=[
            html.H1(children='Math Toolkit Dashboard'),
            html.Div(children=dcc.Dropdown(
                id='math-function-dropdown',
                options=[
                    {'label': 'Add', 'value': 'add'},
                    {'label': 'Subtract', 'value': 'subtract'},
                    {'label': 'Multiply', 'value': 'multiply'},
                    {'label': 'Divide', 'value': 'divide'}
                ],
                value='add',
                style={'width': '50%', 'margin': 'auto', 'display': 'block'}
            ),
            html.Div(children=dcc.Input(
                id='math-input-1',
                type='number',
                value='0',
                style={'width': '50%', 'margin': 'auto', 'display': 'block'}
            ),
            id='math-input-1-container'),
            html.Div(children=dcc.Input(
                id='math-input-2',
                type='number',
                value='0',
                style={'width': '50%', 'margin': 'auto', 'display': 'block'}
            ),
            id='math-input-2-container'),
            html.Div(children=html.Button(
                id='math-calculate-button',
                children='Calculate',
                n_clicks=0
            ),
            id='math-calculate-container'),
            html.Div(id='math-output-container')
        ]
    )
    return app

# Define the callback for math calculation
def math_callback(app):
    @app.callback(
        Output('math-output-container', 'children'),
        [Input('math-calculate-button', 'n_clicks')],
        [State('math-input-1', 'value'), State('math-input-2', 'value'), State('math-function-dropdown', 'value')]
    )
def calculate_math(n_clicks, input_1, input_2, function):
        if n_clicks == 0:  # Prevent the callback from firing on initial load
            raise dash.exceptions.PreventUpdate()
        try:
            if function == 'add':
                result = float(input_1) + float(input_2)
            elif function == 'subtract':
                result = float(input_1) - float(input_2)
            elif function == 'multiply':
                result = float(input_1) * float(input_2)
            elif function == 'divide':
                # Check for division by zero
                if float(input_2) == 0:
                    return 'Error: Division by zero'
                result = float(input_1) / float(input_2)
            return f'Result: {result}'
        except ValueError:  # Handle non-numeric input
            return 'Error: Invalid input'

# Run the app
def run_app():
    app = app_layout()
    math_callback(app)
    app.run_server(debug=True)

if __name__ == '__main__':
    run_app()

"""
Math Toolkit Dashboard
====================

This Dash application provides a simple math toolkit for basic arithmetic operations.

- The 'math-function-dropdown' component allows users to select the desired operation.
- The 'math-input-1' and 'math-input-2' components allow users to input their numbers.
- The 'math-calculate-button' triggers the calculation callback.
- The 'math-output-container' displays the result of the calculation or any error messages.

"""