# 代码生成时间: 2025-09-01 00:25:41
import hashlib
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# 定义哈希值计算工具
class HashCalculator:
    def __init__(self):
        # 初始化Dash应用
        self.app = Dash(__name__)
        self.app.layout = html.Div(children=[
            html.H1('Hash Calculator'),
            dcc.Textarea(
                id='input-text',
                placeholder='Enter text to hash...'
            ),
            html.Div(id='output-container'),
        ])

    # 定义回调函数计算哈希值
    @staticmethod
    def calculate_hash(input_text):
        # 检查输入是否为空
        if not input_text:
            return 'Empty input'
        
        # 计算哈希值
        try:
            hash_object = hashlib.sha256(input_text.encode())
            return hash_object.hexdigest()
        except Exception as e:
            return f'Error: {e}'

    # 定义回调函数更新UI
    @staticmethod
    @Output('output-container', 'children')
    @Input('input-text', 'value')
    def update_output(input_text):
        return HashCalculator.calculate_hash(input_text)

    # 运行Dash应用
    def run(self):
        self.app.run_server(debug=True)

# 主函数
if __name__ == '__main__':
    hash_calculator = HashCalculator()
    hash_calculator.run()