# 代码生成时间: 2025-08-08 20:51:02
import os
import json
from dash import Dash, html, Input, Output
from dash.exceptions import PreventUpdate

# 配置文件管理器类
class ConfigManager:
    def __init__(self, config_file):
        """初始化配置文件管理器
        
        :param config_file: 配置文件路径
        """
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """从文件加载配置"