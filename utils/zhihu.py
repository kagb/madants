#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import time
from PIL import Image

from conf import PC_HEADERS


def get_xsrf(session):
    index_url = 'http://www.zhihu.com'
    index_page = session.get(index_url, headers=PC_HEADERS)
    html = index_page.text
    pattern = r'name="_xsrf" value="(.*?)"'
    _xsrf = re.findall(pattern, html)
    return _xsrf[0]


def get_captcha(session, type='login'):
    t = str(int(time.time()*1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r={0}&type={1}'.format(t, type)
    r = session.get(captcha_url, headers=PC_HEADERS)
    with open('captcha.jpg', 'wb') as f:
        f.write(r.content)
        f.close()
    im = Image.open('captcha.jpg')
    im.show()
    im.close()
    captcha = raw_input("please input the captcha\n>")
    return captcha


def is_login(session):
    url = "https://www.zhihu.com/settings/profile"
    login_code = session.get(url, allow_redirects=False).status_code
    if int(x=login_code) == 200:
        return True
    else:
        return False


def login(session, secret, account):
    post_url = 'http://www.zhihu.com/login/email'
    postdata = {
        '_xsrf': get_xsrf(session),
        'password': secret,
        'remember_me': 'true',
        'email': account,
    }
    r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    if u'登录成功' not in r.text:
        postdata["captcha"] = get_captcha(session)
        r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    session.cookies.save()
    return session


def signup(session, email, secret):
    post_url = 'http://www.zhihu.com/register/email'
    postdata = {
        '_xsrf': get_xsrf(session),
        'password': secret,
        'remember_me': 'true',
        'email': email,
    }
    postdata["captcha"] = get_captcha(session, 'register')
    r = session.post(post_url, data=postdata, headers=PC_HEADERS)
    print r

