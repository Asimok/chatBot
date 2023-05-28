# md5加密盐值
import os
import sqlite3

"""
系统配置
"""
# md5加密盐值
BASE_SALT = "NEUKG"
# 分配API key的最大数量
MAX_KEYS = 10
# API Key合法使用次数
MAX_TIMES = 5
# 管理员邮箱
ADMIN_EMAIL = "adaning@neu.cn"

"""
邮件配置
"""
# 是否选择开启邮件通知功能,True则开启,并填写下面信息
isSendMessage = True
# 设置自己接收信息通知的邮箱
receiver = ["xxx@qq.com", "xxx1@qq.com"]
# 发送邮箱
sender = 'xxx@qq.com'
# 填写发送者的邮箱SMTP授权码
mailPass = '邮箱SMTP授权码'
# smtp服务器
mailHost = 'smtp.qq.com'

"""
数据库配置
"""
BASE_DIR = os.path.dirname("dao/")
db_path = os.path.join(BASE_DIR, "keys.db")
COON = sqlite3.connect(db_path, check_same_thread=False)
