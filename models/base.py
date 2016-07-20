# -*- coding: utf-8 -*-

import datetime

from peewee import DateTimeField, IntegerField, MySQLDatabase
from playhouse.signals import Model


DATABASE = MySQLDatabase('')


class BaseModel(Model, object):

    class Meta:
        database = DATABASE

    id = IntegerField(primary_key=True)
    create_time = DateTimeField(default=datetime.datetime.now)
