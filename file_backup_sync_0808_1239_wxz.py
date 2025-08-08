# 代码生成时间: 2025-08-08 12:39:22
import os
import shutil
import logging
from datetime import datetime

# 设置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileBackupSync:
    def __init__(self, source_folder, backup_folder):
        """
        初始化备份和同步工具
        :param source_folder: 需要备份的源文件夹路径
        :param backup_folder: 备份文件存放的目标文件夹路径
        """
        self.source_folder = source_folder
        self.backup_folder = backup_folder
        
        # 确保备份文件夹存在
        self.ensure_directory(self.backup_folder)

    def ensure_directory(self, path):
        """
        确保目录存在，不存在则创建
        :param path: 目录路径
        """
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Created directory: {path}")

    def backup_files(self):
        """
        备份文件
        """
        for root, dirs, files in os.walk(self.source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                backup_path = self.get_backup_path(file_path)
                try:
                    shutil.copy2(file_path, backup_path)
                    logging.info(f"Backup file: {file_path} to {backup_path}")
                except Exception as e:
                    logging.error(f"Failed to backup file: {file_path}. Error: {e}")

    def get_backup_path(self, file_path):
        """
        获取备份文件的路径
        :param file_path: 源文件路径
        :return: 备份文件路径
        """
        relative_path = os.path.relpath(file_path, self.source_folder)
        return os.path.join(self.backup_folder, relative_path)

    def sync_folders(self):
        """
        同步文件夹
        """
        for root, dirs, files in os.walk(self.source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                backup_path = self.get_backup_path(file_path)
                if not os.path.exists(backup_path):
                    try:
                        shutil.copy2(file_path, backup_path)
                        logging.info(f"Sync file: {file_path} to {backup_path}")
                    except Exception as e:
                        logging.error(f"Failed to sync file: {file_path}. Error: {e}")
                else:
                    file_mtime = os.path.getmtime(file_path)
                    backup_mtime = os.path.getmtime(backup_path)
                    if file_mtime > backup_mtime:
                        try:
                            shutil.copy2(file_path, backup_path)
                            logging.info(f"Sync file: {file_path} to {backup_path} (update)")
                        except Exception as e:
                            logging.error(f"Failed to sync file: {file_path}. Error: {e}")

def main():
    # 设置源文件夹和备份文件夹路径
    source_folder = "/path/to/source"
    backup_folder = "/path/to/backup"

    # 创建文件备份和同步工具实例
    backup_sync_tool = FileBackupSync(source_folder, backup_folder)

    # 执行备份操作
    backup_sync_tool.backup_files()

    # 执行同步操作
    backup_sync_tool.sync_folders()

if __name__ == "__main__":
    main()