from datetime import datetime
import os

# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 访问客户端地址
OPEN_CLIENT_URL = 'https://client.cs.gogotranx.com'