import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender='long@amiam.com'
receivers=['1207549344@qq.com']

#第三方smtp服务
mail_host="mail.amiam.com"
mail_user="long@amiam.com"
mail_pass="xxxxxx"

#三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个utf-8编码
message=MIMEText('python邮件发送测试...','plain','utf-8')
message['From']=Header('zhangbailong','utf-8')
message['To']=Header('测试','utf-8')

subject='Python smtp邮件测试'
message['Subject']=Header(subject,'utf-8')

try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print("邮件发送成功！")
except smtplib.SMTPException:
    print("Error:无法发送邮件。")