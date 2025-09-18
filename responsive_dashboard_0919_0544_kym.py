# 代码生成时间: 2025-09-19 05:44:09
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# 定义一个函数来创建响应式布局的Dash应用
def create_responsive_dashboard():
    # 初始化Dash应用
    app = dash.Dash(__name__)
    
    # 定义应用的布局
    app.layout = html.Div([
        # 添加一个标题
        html.H1("响应式布局Dashboard"),
        
        # 添加一个下拉菜单用于选择数据列
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ["苹果", "香蕉", "橙子"]],
            value="苹果"
        ),
        
        # 添加一个折线图
        dcc.Graph(id='line-graph'),
    ])
    
    # 回调函数，当下拉菜单改变时更新图表
    @app.callback(
        Output('line-graph', 'figure'),
        [Input('dropdown', 'value')]
    )
    def update_graph(selected_dropdown_value):
        try:
            # 读取数据
            df = pd.read_csv('data.csv'on')
            # 根据下拉菜单的值筛选数据
            df = df[df['Fruit'] == selected_dropdown_value]
            # 创建折线图
            fig = px.line(df, x='Year', y='Value', title=f'{selected_dropdown_value}销量趋势')
            return fig
        except Exception as e:
            # 错误处理
            print(f"Error: {e}")
            return px.line().update_layout(title='数据加载失败')
    
    # 运行应用
    if __name__ == '__main__':
        app.run_server(debug=True)

# 创建并运行响应式布局的Dash应用
create_responsive_dashboard()