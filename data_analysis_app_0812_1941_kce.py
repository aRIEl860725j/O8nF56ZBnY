# 代码生成时间: 2025-08-12 19:41:07
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
from dash.exceptions import PreventUpdate

# 定义数据分析器应用
class DataAnalysisApp:
    def __init__(self):
        # 初始化Dash应用
        self.app = dash.Dash(__name__)
        self.app.layout = html.Div(children=[
            html.H1(children='数据分析器'),
            dcc.Upload(
                id='upload-data',
                children=html.Div(['点击上传文件或拖拽到此区域']),
                multiple=False,
                style={'height': '60px', 'lineHeight': '60px', 'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'},
            ),
            html.Div(id='output-data-upload'),
            dcc.Graph(id='data-graph'),
        ])

    def callback_graph(self, data):
        # 处理上传的文件并生成图表
        if data is None:
            raise PreventUpdate

        try:
            df = pd.read_csv(data)
            fig = px.histogram(df, title='数据分布图')
        except Exception as e:
            return html.Div(f'上传文件无效，请上传CSV格式文件。错误详情：{e}')

        return dcc.Graph(figure=fig)

    def register_callbacks(self):
        # 注册回调函数
        @self.app.callback(
            Output('output-data-upload', 'children'),
            [Input('upload-data', 'contents')],
        )
def callback_output(contents):
            if contents is None:
                return PreventUpdate

            try:
                if '.csv' in contents.filename:
                    return html.Div(f'文件 {contents.filename} 已上传，正在解析...')
                else:
                    raise Exception('文件格式不支持')
            except Exception as e:
                return html.Div(f'上传文件无效，请上传CSV格式文件。错误详情：{e}')

        @self.app.callback(
            Output('data-graph', 'figure'),
            [Input('upload-data', 'contents')],
        )
def callback_graph(contents):
            return self.callback_graph(contents)

    def run(self):
        # 运行应用
        self.register_callbacks()
        self.app.run_server(debug=True)

# 实例化并运行数据分析器应用
if __name__ == '__main__':
    app = DataAnalysisApp()
    app.run()