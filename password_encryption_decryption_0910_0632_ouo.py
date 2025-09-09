# 代码生成时间: 2025-09-10 06:32:11
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64
from cryptography.fernet import Fernet

# 初始化Dash应用
app = dash.Dash(__name__)

# 密钥生成和存储
def generate_key():
    return Fernet.generate_key()

# 加密函数
def encrypt_message(message: str, key: bytes) -> str:
    try:
        f = Fernet(key)
        return f.encrypt(message.encode())
    except Exception as e:
        return str(e)

# 解密函数
def decrypt_message(encrypted_message: str, key: bytes) -> str:
    try:
        f = Fernet(key)
        return f.decrypt(encrypted_message).decode()
    except Exception as e:
        return str(e)

# 应用布局
app.layout = html.Div([
    html.H1("Password Encryption Decryption Tool"),
    dcc.Textarea(
        id='input-text',
        placeholder='Enter text to encrypt or decrypt...',
        style={'width': '100%', 'height': '100px'}
    ),
    html.Div(id='output-container'),
    html.Button('Encrypt', id='encrypt-button', n_clicks=0),
    html.Button('Decrypt', id='decrypt-button', n_clicks=0),
    dcc.Download(id='download-link'),
])

# 密钥存储
key = generate_key()

# 回调函数 - 加密按钮点击事件
@app.callback(
    Output('output-container', 'children'),
    Output('download-link', 'href'),
    Input('encrypt-button', 'n_clicks'),
    Input('input-text', 'value'),
    prevent_initial_call=True
)
def encrypt(n_clicks, message):
    if n_clicks > 0 and message:
        encrypted_message = encrypt_message(message, key)
        base64_encrypted = base64.b64encode(encrypted_message).decode()
        return html.Div([
            html.Pre(f'Encrypted: {base64_encrypted}'),
            html.A(
                'Download encrypted message',
                href='data:text/plain;base64,{}'.format(base64_encrypted),
                download='encrypted_message.txt'
            )
        ]), ''
    else:
        return '', ''

# 回调函数 - 解密按钮点击事件
@app.callback(
    Output('output-container', 'children'),
    Input('decrypt-button', 'n_clicks'),
    Input('input-text', 'value'),
    prevent_initial_call=True
)
def decrypt(n_clicks, message):
    if n_clicks > 0 and message:
        try:
            encrypted_message = base64.b64decode(message)
            decrypted_message = decrypt_message(encrypted_message, key)
            return html.Div([
                html.Pre(f'Decrypted: {decrypted_message}')
            ])
        except Exception as e:
            return html.Div([
                html.Pre(f'Error: {str(e)}')
            ])
    else:
        return ''

# 启动Dash应用
if __name__ == '__main__':
    app.run_server(debug=True)