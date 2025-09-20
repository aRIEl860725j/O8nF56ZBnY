# 代码生成时间: 2025-09-20 14:20:45
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px
import os
import re

# 定义主函数
def main():
    # 创建Dash应用
    app = dash.Dash(__name__)

    # 应用布局
    app.layout = html.Div([
        html.H1("日志文件解析工具"),
        dcc.Upload(
            id='upload-data',
            children=html.Div(['拖拽文件到这里或', html.A('选择文件')],),
            style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
                   'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
                   'textAlign': 'center', 'margin': '10px'},
        ),
        dcc.Tabs(id="tabs", value='tab-1', children=[
            dcc.Tab(label='解析结果', value='tab-1'),
            dcc.Tab(label='错误信息', value='tab-2'),
        ]),
        html.Div(id='tabs-content'),
        html.Div(id='error-container')
    ])

    # 回调函数：处理文件上传
    @app.callback(
        Output('tabs-content', 'children'),
        [Input('upload-data', 'contents'),
         Input('upload-data', 'filename')],
    )
    def parse_contents(contents, filename):
        # 检查是否有文件上传
        if contents is None:
            return html.Div([])

        # 保存文件到临时目录
        temp_filename = f"{os.path.splitext(filename)[0]}_{os.urandom(6).hex()}.log"
        with open(temp_filename, 'wb') as f:
            f.write(contents.getbuffer())

        try:
            # 解析日志文件
            df = pd.read_csv(temp_filename, sep=' ', names=['Timestamp', 'Module', 'Message'], engine='python')
            # 清理临时文件
            os.remove(temp_filename)
        except Exception as e:
            # 返回错误信息
            os.remove(temp_filename)
            return html.Div([html.P(f"解析错误：{str(e)}")])

        # 创建解析结果的表格
        figure = px.table(df, title='日志文件解析结果')
        return html.Div([dcc.Graph(figure=figure)])

    # 启动应用
    if __name__ == '__main__':
        app.run_server(debug=True)

# 主函数入口
if __name__ == '__main__':
    main()