# 代码生成时间: 2025-09-16 21:27:28
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output, State
import plotly.express as px

# 数据加载函数
def load_data():
    # 假设数据文件名为data.csv
    return pd.read_csv('data.csv')

# 创建Dash应用
app = dash.Dash(__name__)

# 应用布局
app.layout = html.Div([
    html.H1('数据统计分析器'),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['点击上传数据文件，或拖拽文件到此区域']),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        }
    ),
    dcc.Graph(id='data-visualization'),
    html.Div(id='data-upload-output')
])

# 回调函数，处理上传数据
@app.callback(
    Output('data-upload-output', 'children'),
    Output('data-visualization', 'figure'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is not None:
        try:
            # 读取上传的数据文件
            df = pd.read_csv(
                contents,
                encoding='utf-8'
            )
            # 生成数据可视化图表
            fig = px.histogram(df, x=df.columns[0], nbins=20)
            return html.Div([
                '文件名：', filename,
                '成功上传并加载数据！'
            ]), fig
        except Exception as e:
            print(e)
            return html.Div([
                '数据文件上传失败：', str(e)
            ]), {}
    return html.Div([]), {}

# 运行Dash应用
if __name__ == '__main__':
    app.run_server(debug=True)
