# 代码生成时间: 2025-09-20 01:12:19
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash.exceptions import PreventUpdate
import base64
import io
import os

# 初始化 Dash 应用
app = dash.Dash(__name__)

# 定义布局
app.layout = html.Div([
    # 上传文件的组件
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
        },
    ),
    # 分析结果显示组件
    html.Div(id='output-container', style={'margin': '20px'}),
])

# 定义回调函数，用于处理文件上传和内容分析
@app.callback(
    Output('output-container', 'children'),
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'),
     State('upload-data', 'last_modified')]
)
def update_output(contents, filename, last_modified):
    if contents is None:
        raise PreventUpdate
    # 解码文件内容
    try:
        content_type, content_string = contents.split(',')
        content = base64.b64decode(content_string)
        # 将文件内容读取为字符串
        text = content.decode('utf-8')
        # 将字符串转换为 DataFrame
        df = pd.DataFrame({'text': [text]})
        # 根据需要添加更多的分析逻辑
        # 例如：词频统计
        count = df['text'].str.split().str.len().describe()
        # 将分析结果转换为图表
        fig = px.bar(x=count.index, y=count.values)
        # 将图表保存为 HTML 组件
        fig_div = fig.to_html(full_html=False)
        return html.Div([
            html.H5(filename),
            html.P(f'Last Modified: {last_modified}'),
            html.Iframe(
                id='igraph',
                style={'border-width': '0', 'width': '100%', 'height': '600px'},
                # 将图表的 HTML 内容编码为 base64
                src='data:text/html;base64,' + base64.b64encode(fig_div.encode()).decode()
            ),
        ])
    except Exception as e:
        return html.Div([
            html.H5('Error processing file'),
            html.P(str(e))
        ])

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)