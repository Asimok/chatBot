import sys

from dao.api_key_dao import AuthAPIKey
from config.setting import COON

auth = AuthAPIKey(COON)

# 实现执行 python -m admin.get_key_info k1 命令时，查看key使用情况
if __name__ == '__main__':
    # 从命令行获取参数
    key = sys.argv[1]
    # 更新数据库
    status = auth.get_key_info(key)
    if status:
        print(f'key: {status[0]} , email: {status[1]} , times: {status[2]}')
    else:
        print("查询失败,请检查key")
