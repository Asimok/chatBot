# coding=UTF-8
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import config.setting as config


class SendEmail:

    def __init__(self):
        self.sender = config.sender
        self.receiver = config.receiver
        self.mailHost = config.mailHost
        self.mailUser = config.sender
        self.mailPass = config.mailPass

    def sendMessage(self, user_org, message):
        # 邮件普通文本内容
        mailContent = message
        message = MIMEText(mailContent, 'plain', 'utf-8')
        # 发送人名称
        message['From'] = self.sender
        for user in self.receiver:
            # 收件人名称
            message['To'] = Header(user, 'utf-8')
            # 邮件标题
            message['Subject'] = Header('申请获取API Key', 'utf-8')

            try:
                smtpObj = smtplib.SMTP_SSL(self.mailHost, 465)
                smtpObj.login(self.mailUser, self.mailPass)

                smtpObj.sendmail(self.sender, user, message.as_string())
                print("send emil to : ", user)
            except smtplib.SMTPException:
                print('Error: 无法发送邮件')
                return False
        return True


if __name__ == '__main__':
    _sendEmail = SendEmail()
    _sendEmail.sendMessage('a318', '这是一条测试信息')
