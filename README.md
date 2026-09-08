# UiTest 移动端 UI 自动化测试项目
## 项目介绍
本项目基于 **Appium + Pytest** 实现 APP 自动化测试，采用 **PO 模式（Page Object）** 进行页面封装，结构清晰、易于维护。
适用于：
- Android /iOS APP UI 自动化
- 接口 + UI 混合自动化
- 回归测试、冒烟测试
## 技术栈
- Python 3.8+
- Appium
- Pytest
- Allure 测试报告
- PO 设计模式
## 项目结构
```
UiTest/
├── base/          # 基础基类（driver 封装、元素操作）
├── config/        # 配置文件（设备、APP 信息、路径等）
├── img/           # 图片资源、定位图
├── page/          # 页面对象层
├── pagedata/      # 测试数据
├── tests/         # 测试用例
├── tools/         # 工具类（日志、读取文件等）
├── conftest.py    # Pytest 夹具
├── main.py        # 项目运行入口
├── pytest.ini     # Pytest 配置
├── requirements.txt # 依赖包
├── .gitignore     # Git 忽略文件
└── README.md      # 项目说明
```
## 环境部署

1. 安装 Python 3.8+
2. 安装 Appium Server
3. 安装 Android SDK
4. 安装依赖：
```
pip install -r requirements.txt
```
## 运行方式
### 1. 运行所有用例
```
pytest
```
### 2. 使用 main.py 入口运行
```
python main.py
```
### 3. 生成 Allure 报告
```
pytest --alluredir=report
allure serve report
```
## 输出目录
- log/        运行日志（不上传 GitHub）
- report/     测试报告（不上传 GitHub）
## 注意事项
1. 请勿上传敏感信息（如账号、密码）
2. log、report 为本地运行文件，已加入 .gitignore
3. 配置文件请根据自己设备信息修改
