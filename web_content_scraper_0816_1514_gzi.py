# 代码生成时间: 2025-08-16 15:14:34
import requests
from bs4 import BeautifulSoup
import dash
from dash import dcc, html, Input, Output

# 定义一个函数，用于从给定的URL抓取网页内容
def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        return response.text
    except requests.RequestException as e:
        # 打印错误信息，并且返回None
        print(f"Error fetching web content: {e}")
        return None

# 定义一个函数，用于解析网页内容并提取HTML
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

# 创建Dash应用程序
app = dash.Dash(__name__)

# 定义Dash界面布局
app.layout = html.Div(children=[
    html.H1(children='Web Content Scraper'),
    dcc.Input(id='url-input', type='text', placeholder='Enter URL here'),
    html.Button('Fetch Content', id='fetch-button', n_clicks=0),
    dcc.Markdown(id='output'),
])

# 定义一个回调函数，当用户点击按钮时触发
@app.callback(
    Output('output', 'children'),
    [Input('fetch-button', 'n_clicks')],
    [dash.State('url-input', 'value')]
)
def fetch_content(n_clicks, url):
    if n_clicks > 0:  # 确保按钮被点击了
        html_content = fetch_web_content(url)
        if html_content:
            return html_content  # 返回抓取的HTML内容
        else:
            return "Failed to fetch content."  # 返回失败消息
    return ""  # 如果按钮没有被点击，返回空字符串

# 运行Dash应用程序
if __name__ == '__main__':
    app.run_server(debug=True)