# 代码生成时间: 2025-09-04 19:24:33
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
from dash.exceptions import PreventUpdate

# 定义应用布局
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    # 上传数据文件
    html.Div([
        dcc.Upload(
            id='upload-data',
# 改进用户体验
            children=html.Button('Upload File',
                            id='upload-button',
                            n_clicks=0),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
# 改进用户体验
        ),
        html.Div(id='output-data-upload'),
    ]),
    # 选择图表类型
# 改进用户体验
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['Line', 'Bar', 'Scatter', 'Histogram']],
        value='Line',
        multi=False,
    ),
    # 交互式图表
    dcc.Graph(id='live-update-graph'),
])
# 增强安全性

# 回调函数：处理上传文件
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')]
)
def update_output(list_of_contents):  # 确保list_of_contents不是None
    if list_of_contents is None:  # 如果没有文件被上传
        raise PreventUpdate
    try:  # 尝试读取文件
        df = pd.read_csv(list_of_contents[0])  # 读取第一个文件
    except Exception as e:  # 处理读取文件时的错误
        return f'Error loading file {str(e)}'
    return df.head().to_html(classes='table table-striped')  # 显示文件头部

# 回调函数：根据选择的图表类型更新图表
@app.callback(
    Output('live-update-graph', 'figure'),
    [Input('upload-data', 'filename'), Input('dropdown', 'value')],
    [State('upload-data', 'contents')]
)
def update_graph(filename, chart_type, list_of_contents):  # 确保有文件被上传且选中了图表类型
    if list_of_contents is None or filename is None:  # 如果没有文件被上传或没有选择图表类型
        raise PreventUpdate
    try:  # 尝试读取文件
        df = pd.read_csv(list_of_contents[0])  # 读取第一个文件
# FIXME: 处理边界情况
    except Exception as e:  # 处理读取文件时的错误
        raise PreventUpdate  # 在这种情况下，不更新图表
    # 构建图表数据
    data = []
    if chart_type == 'Line':  # 线图
        data.append(go.Scatter(x=df['x'], y=df['y'], mode='lines+markers'))  # 假设数据包含'x'和'y'列
    elif chart_type == 'Bar':  # 柱状图
        data.append(go.Bar(x=df['x'], y=df['y']))  # 假设数据包含'x'和'y'列
    elif chart_type == 'Scatter':  # 散点图
        data.append(go.Scatter(x=df['x'], y=df['y'], mode='markers'))  # 假设数据包含'x'和'y'列
# TODO: 优化性能
    elif chart_type == 'Histogram':  # 直方图
        data.append(go.Histogram(x=df['y']))  # 假设数据包含'y'列
    # 返回图表配置
    return {
        'data': data,
        'layout': go.Layout(title=f'{chart_type} Chart of {filename}',
                              xaxis={'title': 'X'},
                              yaxis={'title': 'Y'},
                              margin={'l': 40, 'b': 40, 't': 10, 'r': 10})
    }

if __name__ == '__main__':
    app.run_server(debug=True)