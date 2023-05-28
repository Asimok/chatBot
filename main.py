import streamlit as st
from components.sidebar import my_sidebar, get_key_remain_times
from components.disclamier import disclamier
from utils.utils import auth_before_request
from streamlit_chat_media import message

st.set_page_config(page_title="GPTBot", page_icon=":robot_face:")
st.markdown('<style> \
     footer {visibility: hidden;} \
    .css-1n543e5 {float: right;width:100px;}\
    .css-1x8cf1d { \
    display: inline-flex; \
    -webkit-box-align: center; \
    align-items: center; \
    -webkit-box-pack: center; \
    justify-content: center; \
    font-weight: 400; \
    padding: 0.25rem 0.75rem; \
    border-radius: 0.25rem; \
    margin: 0px; \
    line-height: 1.6; \
    color: inherit; \
    width: 100%; \
    height: 100%; \
    user-select: none; \
    background-color: rgb(255, 255, 255); \
    border: 1px solid rgba(49, 51, 63, 0.2); \
    } \
    .css-12w0qpk {\
    transform: translateY(45%); \
    } <style>', unsafe_allow_html=True)

"""
### GPTBot 
"""

my_sidebar()

disclamier()


def reply_function(text, context):
    # TODO 调用API
    context = None
    return '你好，我是GPTBot，我能回答你的问题吗？'
    # return '重复你说的话: ' + text


if 'user' not in st.session_state:
    st.session_state['user'] = []

if 'bot' not in st.session_state:
    st.session_state['bot'] = []
    st.session_state['bot'].append('欢迎使用GPTBot')


def add_message(content, sender):
    if sender == 'bot':
        st.session_state['bot'].append(content)
    else:
        st.session_state['user'].append(content)


col1, col2 = st.columns([3, 1], gap="small")
prompt = col1.text_input("请输入你的问题...")
if col2.button("发送") and auth_before_request() and prompt != "":
    with st.spinner("对话框"):
        msg = reply_function(prompt, None)
        add_message(prompt, 'user')
        add_message(msg, 'bot')

print("bot: ", st.session_state['bot'])
print("user: ", st.session_state['user'])

if 'bot' in st.session_state:
    i = len(st.session_state['bot']) - 1
    l = len(st.session_state['user']) - 1
    if i == 0:
        message(st.session_state['bot'][i], key=str(i), allow_html=True, avatar_style="bottts", seed=100)
    else:
        while i > 0:
            message(st.session_state['bot'][i], key=str(i), allow_html=True, avatar_style="bottts", seed=100)
            message(st.session_state['user'][i - 1], is_user=True, key=str(i) + '_user', allow_html=True,
                    avatar_style="fun-emoji", seed=1521732)
            i -= 1
