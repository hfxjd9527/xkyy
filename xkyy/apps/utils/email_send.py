# -*- coding: utf-8 -*-
# @AuThor  : frank_lee
from random import Random
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from xkyy.settings import EMAIL_FROM


def random_str(random_length=8):
    str = ""
    chars = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    email_recode = EmailVerifyRecord()
    code = random_str(10)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    if send_type == 'register':
        email_title = "星空音乐注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    else:
        if send_type == 'forget':
            email_title = "星空音乐密码重置链接"
            email_body = "请点击下面的重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
            if send_status:
                pass


