import sys

from dao.api_key_dao import AuthAPIKey
from config.setting import COON

auth = AuthAPIKey(COON)

# 实现执行 python -m admin.gen_key_sys utils@163.com 命令时，新增key
if __name__ == '__main__':
    # 从命令行获取参数
    mail = sys.argv[1]
    # 更新数据库
    status = auth.gen_api_sys(mail)
    print(f'{status["data"]}')
