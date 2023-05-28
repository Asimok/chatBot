FROM python:3.9.5-slim-buster
LABEL author="Asimok"
LABEL email="maqi_neu@163.com"
LABEL version="1"

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

RUN mkdir /usr/src/GPTBot -p
COPY . /usr/src/GPTBot
WORKDIR /usr/src/GPTBot
RUN pip install -r requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple
RUN ls
WORKDIR /usr/src/GPTBot
RUN ls
EXPOSE 8051
CMD python -u -m streamlit run main.py --server.port 8051 --browser.gatherUsageStats False