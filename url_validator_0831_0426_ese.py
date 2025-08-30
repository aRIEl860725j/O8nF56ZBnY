# 代码生成时间: 2025-08-31 04:26:31
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from urllib.parse import urlparse
import validators

# URL Validator Function
def is_valid_url(url):
    """Validates if the provided URL is valid or not."""
    try:
        # Check if the URL is valid according to the validators library
        return validators.url(url)
    except Exception as e:
        # If validation fails, return False along with the error message
        print(f"Error validating URL: {str(e)}")
        return False

# Dash App Layout
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("URL Validity Checker"),
    dcc.Input(id='url-input', type='text', placeholder='Enter URL here...'),
    html.Button("Check URL", id='check-url-button', n_clicks=0),
    html.Div(id='output-container')
])

# Callback to Check URL Validity
@app.callback(
    Output('output-container', 'children'),
    [Input('check-url-button', 'n_clicks')],
    [State('url-input', 'value')]
)
def check_url(n_clicks, url_value):
    """Callback function to check if the URL is valid and display the result."""
    if n_clicks > 0:  # Check if the button was clicked
        result = is_valid_url(url_value)
        return f"URL validity: {'Valid' if result else 'Invalid'}
    else:
        return ''  # Return an empty string if the button wasn't clicked

if __name__ == '__main__':
    app.run_server(debug=True)