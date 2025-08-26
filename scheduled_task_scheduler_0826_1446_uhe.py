# 代码生成时间: 2025-08-26 14:46:25
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import datetime
import schedule
import time
from threading import Thread
from flask import current_app

# 定时任务调度器
class ScheduledTaskScheduler:
    def __init__(self):
        # 初始化Dash应用
        self.app = dash.Dash(__name__,
                            external_stylesheets=[dbc.themes.BOOTSTRAP])
        # 设置Dash页面
        self.app.layout = html.Div([
            html.H1("定时任务调度器"),
            html.Button("启动定时任务", id="start-task"),
            html.Button("停止定时任务", id="stop-task"),
            dbc.Alert(id="task-status", is_open=False)
        ])

        # 设置回调函数
        self.app.callback(
            Output("task-status", "is_open"),
            [Input("start-task", "n_clicks")],
            prevent_initial_call=True
        )(input=self.start_task)

        self.app.callback(
            Output("task-status", "is_open"),
            [Input("stop-task", "n_clicks")],
            prevent_initial_call=True
        )(input=self.stop_task)

    def start_task(self, n_clicks):
        # 启动定时任务
        if n_clicks is None:
            raise PreventUpdate
        try:
            # 创建定时任务
            schedule.every(10).seconds.do(self.run_task)
            # 启动调度器
            thread = Thread(target=self.run_scheduler)
            thread.start()
            # 更新任务状态
            return True
        except Exception as e:
            # 处理异常
            current_app.logger.error(f"启动定时任务失败: {str(e)}")
            return False

    def stop_task(self, n_clicks):
        # 停止定时任务
        if n_clicks is None:
            raise PreventUpdate
        try:
            # 停止调度器
            schedule.clear()
            return True
        except Exception as e:
            # 处理异常
            current_app.logger.error(f"停止定时任务失败: {str(e)}")
            return False

    def run_task(self):
        # 执行定时任务
        try:
            # 模拟任务执行
            current_app.logger.info(f"定时任务执行时间: {datetime.datetime.now()}")
        except Exception as e:
            # 处理异常
            current_app.logger.error(f"执行定时任务失败: {str(e)}")

    def run_scheduler(self):
        # 运行调度器
        while True:
            # 执行调度器
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    # 创建定时任务调度器实例
    scheduler = ScheduledTaskScheduler()
    # 运行Dash应用
    scheduler.app.run_server(debug=True)