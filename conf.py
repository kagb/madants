# -*- coding: utf-8 -*-


MYSQL_HOST = ''
MYSQL_USER = ''
MYSQL_PASSWD = ''


try:
    from .local_conf import *
except ImportError:
    pass
