# 代码生成时间: 2025-08-05 06:36:32
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from flask import session
from dash.exceptions import PreventUpdate

# 定义一个简单的用户数据
USERS = {
    "admin": "password123"
}

# 定义Dash应用
app = dash.Dash(__name__)
app.config.suppress_callback_exceptions = True

# 定义用户登录表单布局
login_form = html.Div(
    [
        html.H3("用户登录"),
        dcc.Input(id="username", type="text", placeholder="用户名", autofocus=True),
        dcc.Input(id="password", type="password", placeholder="密码"),
        html.Button("登录", id="login-button", n_clicks=0),
        html.Div(id="login-output"),
    ],
)

# 定义Dash应用布局
app.layout = html.Div([
    login_form
])

# 定义回调函数，处理用户登录逻辑
@app.callback(
    Output("login-output", "children"),
    [Input("login-button", "n_clicks")],
    [State("username", "value"), State("password", "value")],
)
def login(n_clicks, username, password):
    # 如果没有点击登录按钮，则不执行任何操作
    if n_clicks <= 0:
        raise PreventUpdate()
    
    # 检查用户名和密码是否正确
    if username in USERS and USERS[username] == password:
        # 如果登录成功，设置session并返回成功消息
        session["username"] = username
        return f"登录成功，欢迎 {username}！"
    else:
        # 如果登录失败，返回错误消息
        return "用户名或密码错误，请重新输入。"

# 运行Dash应用
if __name__ == '__main__':
    app.run_server(debug=True)