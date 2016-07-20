# -*- coding: utf-8 -*-


MYSQL_DB_NAME = 'madants'
MYSQL_HOST = 'localhost'
MYSQL_USER = 'madqueen'
MYSQL_PASSWD = ''


try:
    from local_conf import *
except ImportError:
    pass
