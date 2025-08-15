# 代码生成时间: 2025-08-16 01:02:29
# math_calculator.py
"""
A simple Dash application that serves as a math calculator with basic operations.
"""

import dash
def add(x, y):
    """Add two numbers.
    
    Args:
        x (int or float): First number.
        y (int or float): Second number.
    
    Returns:
        int or float: The sum of x and y.
    """
    return x + y
def subtract(x, y):
    """Subtract two numbers.
    
    Args:
        x (int or float): Minuend.
        y (int or float): Subtrahend.
    
    Returns:
        int or float: The difference between x and y.
    """
    return x - y
def multiply(x, y):
    """Multiply two numbers.
    
    Args:
        x (int or float): First number.
        y (int or float): Second number.
    
    Returns:
        int or float: The product of x and y.
    """
    return x * y
def divide(x, y):
    """Divide two numbers.
    
    Args:
        x (int or float): Dividend.
        y (int or float): Divisor.
    
    Returns:
        int or float: The quotient of x and y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Define a dictionary to map math operations to their corresponding functions.
MATH_OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# Create a Dash application.
app = dash.Dash(__name__)

# Define the layout of the Dash application.
app.layout = dash.html.Div([
    dash.html.H1("Math Calculator"),
    dash.html.Div([
        dash.html.Label("First number: "),
        dash.html.Input(id="first-num", type="number")
    ]),
    dash.html.Div([
        dash.html.Label("Second number: "),
        dash.html.Input(id="second-num", type="number")
    ]),
    dash.html.Div([
        dash.html.Label("Operation: "),
        dash.html.Select(id="operation", options=[
            {'label': op, 'value': op} for op in MATH_OPERATIONS.keys()
        ])
    ]),
    dash.html.Button("Calculate", id="calculate-btn"),
    dash.html.Div(id="result")
])

# Define a callback to update the result.
@app.callback(
    dash.dependencies.Output("result", "children"),
    dash.dependencies.Input("calculate-btn", "n_clicks"),
    [dash.dependencies.State("first-num", "value"), dash.dependencies.State("second-num", "value"), dash.dependencies.State("operation", "value")]
)
def calculate(n_clicks, first_num, second_num, operation):
    if n_clicks is None or not first_num or not second_num:
        return ""  # Return an empty string if inputs are not provided.
    try:
        result = MATH_OPERATIONS[operation](float(first_num), float(second_num))
    except ValueError as e:
        return str(e)
    except Exception:
        return "An error occurred."
    return f"The result is: {result}"

# Run the Dash application.
if __name__ == '__main__':
    app.run_server(debug=True)