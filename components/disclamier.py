import streamlit as st

clamier = """
该项目仅供学习交流使用，禁止用于商业用途。在使用过程中，使用者需认真阅读并遵守以下声明:

1. 本项目仅为大模型测试功能而生，使用者需自行承担风险和责任，如因使用不当而导致的任何损失或伤害，本项目概不负责；
2. 本项目可能涉及的知识产权，如有侵犯，请及时联系我们，我们将及时删除相关内容；
3. 本项目中出现的第三方链接或库仅为提供便利而存在，其内容和观点与本项目无关。使用者在使用时需自行辨别，本项目不承担任何连带责任；
4. 使用者在测试和使用模型时，应遵守相关法律法规，如因使用不当而造成损失的，本项目不承担责任，使用者应自行承担；若项目出现任何错误，请务必及时向我方反馈，以助于我们及时修复；
5. 本项目所包含的所有信息均为开放式知识，如有任何误导、错误或不完整问题，请及时联系我们更正；
6. 本模型中出现的任何违反法律法规或公序良俗的回答，均不代表本项目观点和立场，我们将不断完善模型回答以使其更符合社会伦理和道德规范。

使用本项目即表示您已经仔细阅读、理解并同意遵守以上免责声明。本项目保留在不预先通知任何人的情况下修改本声明的权利。
"""

def _check_call():
    st.session_state.check_flag = True

def disclamier(clamier=clamier):
    check_flag = False
    ph = st.empty()

    if 'check_flag' not in st.session_state:
        st.session_state.check_flag = False

    with ph.container():
        with ph.expander('**免责声明**', expanded=True):
            st.markdown(clamier)
            check_flag = st.checkbox('已阅读并同意上述声明', key='check1', on_change=_check_call)
            if not st.session_state.check_flag:
                st.warning('请先阅读并同意免责声明')
                st.stop()
            
    
    if st.session_state.check_flag:
        ph.empty()
        with ph.container():
            with ph.expander('**免责声明**', expanded=False):
                st.markdown(clamier)
                st.checkbox('已阅读并同意上述声明', key='check2', value=True, disabled=True)