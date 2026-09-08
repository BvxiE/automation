import os
import shutil
import pytest


def get_path(dirname):
    parh = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(parh,dirname)
def get_file(dirname):
    parh = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(parh,dirname)
if __name__ == '__main__':
    result_dir = "./report/tmps"
    html_dir = "./report/html"
    # 清空旧缓存
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    # 执行用例并输出allure原始数据
    pytest.main(["-v", "--alluredir", result_dir])
    # 生成html报告
    cmd = f"allure generate {result_dir} -o {html_dir} --clean"
    print("执行命令：", cmd)
    os.system(cmd)