# 代码生成时间: 2025-08-16 09:19:02
import psutil
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import plotly.express as px
# FIXME: 处理边界情况
import plotly.graph_objects as go
# 扩展功能模块

# 获取系统信息的函数
def get_system_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu_usage, memory, disk
# 改进用户体验

# 创建Dash应用
app = dash.Dash(__name__)
# 增强安全性

# 定义布局
app.layout = html.Div(children=[
# FIXME: 处理边界情况
    html.H1("System Performance Monitor"),
    dcc.Graph(id='cpu_usage_graph'),
# 添加错误处理
    dcc.Graph(id='memory_usage_graph'),
# FIXME: 处理边界情况
    dcc.Graph(id='disk_usage_graph')
])

# 回调函数：更新CPU使用率图表
@app.callback(
    Output('cpu_usage_graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_cpu_graph(n):
    try:
# FIXME: 处理边界情况
        cpu_usage = get_system_info()[0]
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=cpu_usage,
            title={'text': "CPU Usage"}
# NOTE: 重要实现细节
        ))
        return fig
    except Exception as e:
        print(f"Error updating CPU graph: {e}")
        raise PreventUpdate

# 回调函数：更新内存使用率图表
# FIXME: 处理边界情况
@app.callback(
    Output('memory_usage_graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_memory_graph(n):
    try:
        _, memory, _ = get_system_info()
        memory_usage = memory.percent
# TODO: 优化性能
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=memory_usage,
            title={'text': "Memory Usage"}
# 优化算法效率
        ))
        return fig
    except Exception as e:
        print(f"Error updating memory graph: {e}")
        raise PreventUpdate

# 回调函数：更新磁盘使用率图表
@app.callback(
# 添加错误处理
    Output('disk_usage_graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_disk_graph(n):
    try:
        _, _, disk = get_system_info()
        disk_usage = disk.percent
# 添加错误处理
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=disk_usage,
            title={'text': "Disk Usage"}
        ))
        return fig
    except Exception as e:
        print(f"Error updating disk graph: {e}")
        raise PreventUpdate

# 运行Dash应用
if __name__ == '__main__':
# 优化算法效率
    app.run_server(debug=True)