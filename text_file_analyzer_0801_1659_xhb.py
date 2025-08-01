# 代码生成时间: 2025-08-01 16:59:45
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate
from pathlib import Path
import base64
import io

# 主页面布局
def main_layout():
    return html.Div(children=[
        html.H1(children='Text File Analyzer'),
        html.Div(children=[
            dcc.Upload(
                id='upload-data',
                children=html.Div(["Drag and Drop or ", html.A('Select a File')]),
                style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                        'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                        'textAlign': 'center', 'margin': '10px'},
                # 允许上传多个文件
                multiple=True
            ),
            html.Div(id='output-data-upload', style={'fontSize': '20', 'fontWeight': 'bold'})
        ]),
        html.Div(id='file-content-display')
    ])

# 回调函数触发文件上传事件
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')])
def update_output(entered, list_of_names, list_of_dates):
    if entered is None:
        raise PreventUpdate

    children = ''
    for name, date in zip(list_of_names, list_of_dates):
        children += f'{name} ({date})<br>'

    return children

# 回调函数显示文件内容
@app.callback(
    Output('file-content-display', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')])
def display_content(entered, list_of_names, list_of_dates):
    if entered is None:
        raise PreventUpdate

    children = []
    for name, date in zip(list_of_names, list_of_dates):
        children.append(html.H6(f'File: {name}'))
        children.append(html.P(f'Date: {date}'))
        children.append(html.Hr())
        try:
            content_type, content_string = entered.split(',')
            decoded = base64.b64decode(content_string)
            try:
                if 'csv' in name:
                    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
                    figure = px.histogram(df, title=name)
                    children.append(dcc.Graph(figure=figure))
                else:
                    children.append(html.Pre(decoded.decode('utf-8')))
            except Exception as e:
                children.append(html.Div(str(e)))
        except Exception as e:
            children.append(html.Div(str(e)))

    return children

# 定义Dash应用
app = dash.Dash(__name__)

# 设置应用布局
app.layout = main_layout()

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)