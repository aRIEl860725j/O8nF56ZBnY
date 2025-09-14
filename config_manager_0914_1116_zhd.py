# 代码生成时间: 2025-09-14 11:16:15
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import yaml
import os

# Constants
DEFAULT_CONFIG_FILE = 'default_config.yaml'
CONFIG_FILE_PATH = 'config/'

# Helper function to load configuration file
def load_config(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        raise Exception(f"Configuration file not found: {file_path}")
    except yaml.YAMLError as e:
        raise Exception(f"Error parsing YAML file: {e}")

# Helper function to save configuration
def save_config(config, file_path):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(config, file)
    except Exception as e:
        raise Exception(f"Error saving configuration: {e}")

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1(children='Config Manager'),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ',
                       html.A('Select Config File')],
                       style={'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                              'textAlign': 'center', 'margin': '2px'}),
        style={'width': '50%', 'height': '60px', 'lineHeight': '60px',
               'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px'},
    ),
    html.Div(id='output-data-upload'),
    html.Button('Save Config', id='save-config-button', n_clicks=0),
    dcc.Textarea(id='config-editor', style={'width': '100%', 'height': '300px'}),
])

# Callback to display the uploaded file name
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'filename')],
    [State('upload-data', 'contents')]
)
def display_filename(filename, contents):
    if filename:
        # Load the config from the uploaded file
        config = load_config('config/' + filename)
        # Update the config editor with the loaded config
        return html.Div([html.H5(filename), dcc.Textarea(value=yaml.dump(config, default_flow_style=False))])
    else:
        return ''

# Callback to save the configuration
@app.callback(
    Output('config-editor', 'value'),
    [Input('save-config-button', 'n_clicks')],
    [State('config-editor', 'value')]
)
def save_configuration(n_clicks, config_value):
    if n_clicks > 0 and config_value:
        try:
            # Convert the config value back to a dictionary
            config = yaml.safe_load(config_value)
            # Save the config to the default file
            save_config(config, os.path.join(CONFIG_FILE_PATH, DEFAULT_CONFIG_FILE))
            return f'Config saved to {DEFAULT_CONFIG_FILE}'
        except Exception as e:
            return str(e)
    return config_value

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)