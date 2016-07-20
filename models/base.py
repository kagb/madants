# -*- coding: utf-8 -*-

import datetime

from peewee import DateTimeField, IntegerField, MySQLDatabase
from playhouse.signals import Model

from madants.conf import MYSQL_HOST, MYSQL_PASSWD, MYSQL_USER


DATABASE = MySQLDatabase('')


class BaseModel(Model, object):

    class Meta:
        database = DATABASE

    id = IntegerField(primary_key=True)
    create_time = DateTimeField(default=datetime.datetime.now)
