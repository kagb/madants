# -*- coding: utf-8 -*-

import datetime

from peewee import DateTimeField, PrimaryKeyField, MySQLDatabase
from playhouse.signals import Model

from conf import MYSQL_DB_NAME, MYSQL_HOST, MYSQL_PASSWD, MYSQL_USER

DATABASE = MySQLDatabase(
    MYSQL_DB_NAME,
    user=MYSQL_USER,
    host=MYSQL_HOST,
    passwd=MYSQL_PASSWD
)


class BaseModel(Model, object):

    domain = 'BaseModel'

    class Meta(object):
        database = DATABASE

    id = PrimaryKeyField(primary_key=True)
    create_time = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return '<domain={0}, id={1}, create_time={2}>'.format(
            self.domain,
            self.id,
            self.create_time,
        )
