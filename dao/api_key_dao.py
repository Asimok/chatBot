import _md5

from utils.utils import validate_email
from config.setting import BASE_SALT, MAX_KEYS, MAX_TIMES, COON, ADMIN_EMAIL


class AuthAPIKey:
    def __init__(self, coon):
        self.conn = coon
        self.c = self.conn.cursor()
        # 判断数据表 api_keys 是否存在 不存在则创建
        self.c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='api_keys'")
        result = self.c.fetchone()
        if result is not None:
            print("数据表 api_keys 已存在")
        else:
            print("数据表 api_keys 不存在,即将创建")
            self.c.execute(
                '''CREATE TABLE IF NOT EXISTS api_keys (key TEXT PRIMARY KEY, email TEXT ,time INTEGER)''')

    def gen_api_key(self, mail):
        # 根据邮箱生成key
        # 使用md5实现
        md5_keys = _md5.md5((mail + BASE_SALT).encode('utf-8')).hexdigest()
        # 查询是否存在数据库
        self.c.execute("SELECT time FROM api_keys WHERE key = ?", (md5_keys,))

        key = self.c.fetchone()
        if key is None:
            # 判断数据条数
            self.c.execute("SELECT key FROM api_keys ")
            count = self.c.fetchall()
            if len(count) >= MAX_KEYS:
                return {"status": -1, "data": "API key已经分配完了，请联系{}".format(ADMIN_EMAIL)}
            # 插入
            self.c.execute("INSERT INTO api_keys (key, email,time) VALUES (?, ?, ?)", (md5_keys, mail, MAX_TIMES))
            self.conn.commit()
            return {"status": 1, "data": md5_keys}

        else:
            # 禁止重复申请
            return {"status": 0, "data": "请不要重复申请!"}

    def gen_api_sys(self, mail):
        # 校验邮箱
        if not validate_email(mail):
            return {"status": 1, "data": "请核对您的邮箱!"}
        # 申请key
        return self.gen_api_key(mail)

    def get_api_key(self, mail):
        # 申请key
        return self.gen_api_key(mail)

    def get_key_info(self, key):
        # 获取key的信息
        self.c.execute("SELECT * FROM api_keys WHERE key = ?", (key,))
        key_info = self.c.fetchone()
        if key_info:
            return key_info
        else:
            return False

    def get_key_remain_times(self, key):
        # 获取key剩余次数
        self.c.execute("SELECT time FROM api_keys WHERE key = ?", (key,))
        time = self.c.fetchone()
        if time:
            return time[0]
        else:
            return -1

    def update_api_key(self, key, time):
        # 减少次数
        try:
            self.c.execute("UPDATE api_keys SET time = ? WHERE key = ?", (time - 1, key))
            self.conn.commit()
            return True
        except:
            return False

    def reset_api_key(self, key):
        # 重置次数
        try:
            # 查询是否存在
            self.c.execute("SELECT time FROM api_keys WHERE key = ?", (key,))
            time = self.c.fetchone()
            if time is None:
                print("不存在该key")
                return False
            self.c.execute("UPDATE api_keys SET time = ? WHERE key = ?", (MAX_TIMES, key))
            self.conn.commit()
            return True
        except:
            return False

    def del_api_key(self, key):
        # 删除key
        try:
            self.c.execute("DELETE FROM api_keys WHERE key = ?", (key,))
            self.conn.commit()
            return True
        except:
            return False

    def auth_api_key(self, key):
        # 验证key是否可用
        self.c.execute("SELECT time FROM api_keys WHERE key = ?", (key,))
        time = self.c.fetchone()
        print(key, time)
        if time:
            if time[0] > 0:
                while True:
                    if self.update_api_key(key, time[0]):
                        break
                return True
            return False
        else:
            return False


if __name__ == '__main__':
    auth = AuthAPIKey(COON)
    # auth.create_dataset(10, 3)
    # print(auth.get_api_key())
    # print(auth.auth_api_key('926ff2ce62c0632f3f39c898061daaf9'))
    # print(auth.gen_api_key("2121"))
    # print(auth.reset_api_key('k1'))
    # print(auth.get_key_info('k1'))
    print(auth.gen_api_sys("123@123.com"))
