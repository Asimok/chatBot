import streamlit as st

from dao.api_key_dao import AuthAPIKey
from components.faq import faq
from utils.utils import validate_email
from config.setting import COON
from utils.sendMail import SendEmail

_sendEmail = SendEmail()
_auth = AuthAPIKey(COON)


def get_key_remain_times():
    _remain_times = _auth.get_key_remain_times(st.session_state.get("GPTBot_API_KEY", ""))
    if _remain_times == -1:
        return "请先填写正确的API Key"
    return "API Key 剩余使用次数: {}".format(_remain_times)


def set_GPTBot_api_key(api_key: str):
    st.session_state["GPTBot_API_KEY"] = api_key
    st.session_state["REMAIN_TIMES"] = get_key_remain_times()
    # st.session_state.update(["REMAIN_TIMES", get_key_remain_times()])
    print("更新GPTBot_API_KEY: ", st.session_state["GPTBot_API_KEY"])
    print("剩余次数: ", st.session_state["REMAIN_TIMES"])


def apply_api_key():
    name = st.text_input('姓名')
    # 获取用户输入的组织机构
    organization = st.text_input('组织机构')
    # 获取用户输入的手机号码
    phone = st.text_input('手机号')
    # 获取用户输入的邮箱地址
    email = st.text_input('邮箱')

    # 获取用户输入的申请理由
    reason = st.text_area('申请理由')

    if st.button('提交申请', use_container_width=True):
        if not validate_email(email):
            st.error("请核对您的邮箱!")
            return
        _gen_api_key = _auth.gen_api_key(email)
        print(_gen_api_key)
        if _gen_api_key["status"] == -1:
            st.error(_gen_api_key["data"])
        elif _gen_api_key["status"] == 0:
            st.error(_gen_api_key["data"])
        else:
            body = f'您好，我是{name} ,来自 {organization}  手机号: {phone}  邮箱: {email}  申请获取API密钥。\n申请理由是：{reason}\n' \
                   f'系统希望分配给 {name} 的API Key是: {_gen_api_key["data"]}'
            status = _sendEmail.sendMessage(name + '_' + organization, body)
            if status:
                st.success('提交成功！请等待审核。')
            else:
                # 删除数据库中的数据
                _auth.del_api_key(_gen_api_key["data"])
                st.error('提交失败！请重新尝试。')


def my_sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [GPTBot API key] below🔑\n"
            "2. Enter text \n"
        )

        api_key_input = st.text_input(
            "GPTBot API Key",
            type="password",
            placeholder="请输入 GPTBot API key",
            help="点击下方 申请体验 获取API Key",
            value=st.session_state.get("GPTBot_API_KEY", ""),
        )

        if api_key_input:
            set_GPTBot_api_key(api_key_input)

        if st.session_state.get("REMAIN_TIMES", "") != "":
            st.success(st.session_state.get("REMAIN_TIMES", ""))

        with st.expander("申请体验"):
            apply_api_key()

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖GPTBot allows you to ... (There will be continued writing by Adaning et.) "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown("Made by Asimok and His bro Abel 2023-5-6")
        st.markdown("---")

        # faq()
