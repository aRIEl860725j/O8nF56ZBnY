# 代码生成时间: 2025-09-18 13:35:26
import json
import os
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

"""
配置文件管理器
"""

# 配置文件路径
CONFIG_FILE_PATH = 'config.json'

# 读取配置文件
def read_config(filepath):
    """
    读取配置文件
    :param filepath: 配置文件路径
    :return: 配置文件内容
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'配置文件 {filepath} 不存在')
    
    with open(filepath, 'r') as f:
        return json.load(f)

# 保存配置文件
def save_config(filepath, config):
    """
    保存配置文件
    :param filepath: 配置文件路径
    :param config: 配置文件内容
    """
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

# 创建 Dash 应用
app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

# 添加页面布局
app.layout = html.Div([
    # 配置文件路径输入框
    dcc.Input(id='config-file-path', type='text', placeholder='输入配置文件路径'),
    
    # 读取配置文件按钮
    html.Button('读取配置文件', id='read-config-btn', n_clicks=0),
    
    # 配置文件内容显示区域
    html.Pre(id='config-content'),
    
    # 配置文件内容编辑区域
    dcc.Textarea(id='config-editor', style={'width': '100%', 'height': '300px'}),
    
    # 保存配置文件按钮
    html.Button('保存配置文件', id='save-config-btn', n_clicks=0)
])

# 读取配置文件回调函数
@app.callback(
    Output('config-content', 'children'),
    [Input('read-config-btn', 'n_clicks')],
    [State('config-file-path', 'value')]
)
def read_config_callback(n_clicks, filepath):
    if n_clicks == 0:
        return ''
    try:
        config = read_config(filepath)
        return json.dumps(config, indent=4)
    except Exception as e:
        return str(e)

# 保存配置文件回调函数
@app.callback(
    Output('config-editor', 'value'),
    [Input('save-config-btn', 'n_clicks')],
    [State('config-editor', 'value'), State('config-file-path', 'value')]
)
def save_config_callback(n_clicks, config, filepath):
    if n_clicks == 0:
        return ''
    try:
        save_config(filepath, json.loads(config))
        return json.dumps({'message': '配置文件保存成功'}, indent=4)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run_server(debug=True)