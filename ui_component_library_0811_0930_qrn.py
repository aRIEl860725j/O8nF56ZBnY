# 代码生成时间: 2025-08-11 09:30:48
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# 创建Dash应用
app = dash.Dash(__name__)

# 定义应用的布局
app.layout = html.Div([
    # 标题
    html.H1("用户界面组件库"),

    # 输入组件
    dcc.Input(id='input-component', type='text', placeholder='输入文本'),
    # 输入框组件
    dcc.Textarea(id='textarea-component', placeholder='输入文本'),
    # 复选框组件
    dcc.Checklist(
        id='checklist-component',
        options=[{'label': '选项1', 'value': 'option1'},
                 {'label': '选项2', 'value': 'option2'}],
        value=['option1']
    ),
    # 下拉菜单组件
    dcc.Dropdown(
        id='dropdown-component',
        options=[{'label': '选项1', 'value': 'option1'},
                 {'label': '选项2', 'value': 'option2'}],
        value='option1'
    ),
    # 单选按钮组组件
    dcc.RadioItems(
        id='radioitems-component',
        options=[{'label': '选项1', 'value': 'option1'},
                 {'label': '选项2', 'value': 'option2'}],
        value='option1'
    ),
    # 按钮组件
    html.Button('点击按钮', id='button-component'),
    # 显示按钮点击次数的输出组件
    html.Div(id='output-component')
])

# 回调函数：按钮点击次数
@app.callback(
    Output('output-component', 'children'),
    [Input('button-component', 'n_clicks')]
)
def update_output(n_clicks):
    if n_clicks is None:
        return '0' # 初始状态返回0
    else:
        return f'{n_clicks}' # 返回按钮点击次数

# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)