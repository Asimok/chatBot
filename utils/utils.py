import re

import streamlit as st

from config.setting import COON


# 验证邮箱是否合法
def validate_email(email):
    # 正则表达式匹配邮箱格式
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False


def auto_key_configured():
    if not st.session_state.get("GPTBot_API_KEY"):
        print("从左侧栏获取GPTBot API密钥")
        return False
    else:
        print("GPTBot_API_KEY: ", st.session_state["GPTBot_API_KEY"])
        return True


def auth_before_request():
    if auto_key_configured():
        # st.write("GPTBot_API_KEY: ", st.session_state["GPTBot_API_KEY"])
        # 验证GPTBot_API_KEY是否有效
        from dao.api_key_dao import AuthAPIKey
        _auth = AuthAPIKey(COON)
        if not _auth.auth_api_key(st.session_state["GPTBot_API_KEY"]):
            st.error("GPTBot_API_KEY 无效，请重新输入!")
            return False
        return True
    else:
        print("GPTBot_API_KEY 未配置")
        st.error("GPTBot_API_KEY 未配置!")
        return False
