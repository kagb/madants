# -*- coding: utf-8 -*-


MYSQL_HOST = ''
MYSQL_USER = ''
MYSQL_PASSWD = ''


try:
    from .local_config import *
except ImportError:
    pass
