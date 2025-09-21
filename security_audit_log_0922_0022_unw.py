# 代码生成时间: 2025-09-22 00:22:33
import os
from datetime import datetime
from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
from dash import Dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# 配置日志
LOG_FILENAME = 'security_audit.log'
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(LOG_FILENAME),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Flask应用和Dash应用
app = Flask(__name__)
server = Dash(__name__, server=app, routes_pathname_prefix='/dash/')

# 定义Dash应用布局
app.layout = html.Div([
    html.H1('Security Audit Log Dashboard'),
    dcc.Graph(id='log-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    html.Div(id='log-output')
])

# 回调函数：更新日志图表
@server.callback(
    Output('log-graph', 'figure'),
    [Input('interval-component', 'n_intervals')])
def update_graph(n):
    # 读取日志文件内容
    log_entries = []
    with open(LOG_FILENAME, 'r') as file:
        for line in file:
            log_entries.append(line.strip())
    # 返回图表
    return {
        'data': [{'x': [entry.split(' - ')[0] for entry in log_entries],
                  'y': [float(entry.split(' - ')[2].split(' ')[1]) for entry in log_entries]}],
        'layout': {'title': 'Security Audit Log'}
    }

# 回调函数：输出日志内容到Dash应用
@server.callback(
    Output('log-output', 'children'),
    [Input('interval-component', 'n_intervals')])
def update_log_output(n):
    # 读取日志文件内容
    log_entries = []
    with open(LOG_FILENAME, 'r') as file:
        for line in file:
            log_entries.append(html.P(line))
    # 返回日志内容
    return log_entries

# 处理请求并记录日志
@app.route('/log', methods=['POST'])
def log_request():
    try:
        # 获取请求数据
        data = request.json
        # 记录日志
        logger.info(f'Request from {data[