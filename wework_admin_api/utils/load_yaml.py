import yaml


def get_data(file_path):
    # 读取yaml文件
    with open(file_path, encoding="utf-8") as f:
        return yaml.safe_load(f)