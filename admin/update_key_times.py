import sys

from dao.api_key_dao import AuthAPIKey
from config.setting import COON

auth = AuthAPIKey(COON)

# 实现执行 python -m admin.update_key_times k1 命令时，更新数据库中的次数
if __name__ == '__main__':
    # 从命令行获取参数
    key = sys.argv[1]
    # 更新数据库
    status = auth.reset_api_key(key)
    if status:
        print("更新成功")
    else:
        print("更新失败")
