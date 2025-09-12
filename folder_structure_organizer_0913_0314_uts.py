# 代码生成时间: 2025-09-13 03:14:24
import os
import shutil
from dash import Dash, html, dcc, Input, Output

# 定义一个文件夹结构整理器的类
class FolderStructureOrganizer:
    def __init__(self, directory):
        """
        初始化目录
        :param directory: 需要整理的目录路径
        """
        self.directory = directory
        self.errors = []  # 存储错误信息

    def validate_directory(self):
        """
        验证目录是否存在
        """
        if not os.path.exists(self.directory):
            self.errors.append(f"The directory {self.directory} does not exist.")
            return False
        return True

    def list_files(self):
        """
        列出目录下所有文件和文件夹
        """
        if not self.validate_directory():
            return None

        files_and_dirs = []
        for item in os.listdir(self.directory):
            files_and_dirs.append(item)
        return files_and_dirs

    def organize(self):
        """
        整理目录结构
        """
        if not self.validate_directory():
            return None

        # 定义目标文件夹结构
        target_folders = {
            'docs': ['*.txt', '*.docx'],
            'images': ['*.png', '*.jpg', '*.jpeg', '*.gif'],
            'videos': ['*.mp4', '*.mov', '*.avi'],
            'archives': ['*.zip', '*.rar', '*.tar', '*.gz'],
            'others': []  # 其他未匹配文件
        }

        for item in os.listdir(self.directory):
            for folder, patterns in target_folders.items():
                for pattern in patterns:
                    if fnmatch.fnmatch(item, pattern):
                        source_path = os.path.join(self.directory, item)
                        target_path = os.path.join(self.directory, folder, item)
                        os.makedirs(os.path.dirname(target_path), exist_ok=True)
                        shutil.move(source_path, target_path)
                        break
            else:
                # 如果文件没有匹配到任何模式，则移动到others文件夹
                others_path = os.path.join(self.directory, 'others', item)
                os.makedirs(os.path.dirname(others_path), exist_ok=True)
                shutil.move(os.path.join(self.directory, item), others_path)

    def get_errors(self):
        """
        获取错误信息
        """
        return self.errors

# Dash 应用
app = Dash(__name__)
app.layout = html.Div([
    dcc.Upload(id='upload-data', children=html.Button("Upload Folder Path"),
               multiple=False),
    html.Div(id='output-data-upload')
])

@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents'))
def update_output(contents):
    if contents is not None:
        directory = contents.split(b'\x00')[0].decode('utf-8')
        organizer = FolderStructureOrganizer(directory)
        try:
            organizer.organize()
        except Exception as e:
            return f'An error occurred: {str(e)}'

        errors = organizer.get_errors()
        if errors:
            return f'Errors occurred: {errors}'
        return 'Folder structure organized successfully!'
    return None

if __name__ == '__main__':
    app.run_server(debug=True)
