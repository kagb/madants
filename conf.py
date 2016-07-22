# -*- coding: utf-8 -*-


MYSQL_DB_NAME = 'madants'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'madqueen'
MYSQL_PASSWD = ''
CAPTCHA_PATH = 'captcha.jpg'


PC_USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
PC_HEADERS = {
    'User-Agent': PC_USER_AGENT,
}


try:
    from local_conf import *
except ImportError:
    pass
