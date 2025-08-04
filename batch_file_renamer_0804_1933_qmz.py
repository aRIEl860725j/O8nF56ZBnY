# 代码生成时间: 2025-08-04 19:33:01
import os
# 增强安全性
from pathlib import Path
import dash
# 优化算法效率
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# 定义全局变量，存储文件路径和文件名
global current_directory
# FIXME: 处理边界情况
current_directory = None

# 文件重命名函数
def rename_files(prefix, directory):
    """批量重命名指定目录下的所有文件"""
    try:
        # 检查目录是否存在
        if not os.path.exists(directory):
            raise ValueError("Directory does not exist.")
        
        # 遍历目录下的所有文件
        for filename in os.listdir(directory):
            # 生成新的文件名
            new_filename = f"{prefix}_{filename}"
            
            # 重命名文件
# TODO: 优化性能
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")
    except Exception as e:
        print(f"Error renaming files: {e}")

# Dash 应用布局
# NOTE: 重要实现细节
app = dash.Dash(__name__)
# 扩展功能模块

app.layout = html.Div(children=[
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ',
                       html.A('Select Files')]),
# TODO: 优化性能
        style={"width": '100%', "height": '60px', "lineHeight": '60px',
                "borderWidth": '1px', 'borderStyle': 'dashed', 'borderRadius': '5px'},
        # 允许上传多个文件
        multiple=True
    ),
    html.Div(id='output-data-upload')
])

# 回调函数，处理上传的文件并重命名
@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents')]
)
def update_output(contents):
# 改进用户体验
    global current_directory
# 优化算法效率
    
    if contents is not None:
        # 读取上传的文件路径
        file_path = contents[0]['filename']
        file_directory = Path(file_path).parent
        
        # 获取文件前缀
        prefix = Path(file_path).stem
        
        # 调用重命名函数
        rename_files(prefix, str(file_directory))
        
        # 更新全局变量
        current_directory = str(file_directory)
        
        # 返回重命名结果
        return html.Div([
            f"Files in {file_directory} have been renamed with prefix {prefix}."
        ])
    else:
        return html.Div([
            "Drag and drop a file into the box or click to select a file to upload."
        ])
# 改进用户体验

# 运行Dash应用
if __name__ == '__main__':
    app.run_server(debug=True)