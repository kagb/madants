# -*- coding: utf-8 -*-

from peewee import CharField, ForeignKeyField

from model.base import BaseModel


class Army(BaseModel):

    domain = 'Army'

    class Meta(object):
        db_table = 'army'

    name = CharField()
    home = CharField()


class SubArmy(BaseModel):

    domain = 'SubArmy'

    class Meta(object):
        db_table = 'subarmy'

    name = CharField()
    home = CharField()
    army = ForeignKeyField(Army, related_name='subarmies')


class Ant(BaseModel):

    domain = 'Ant'

    class Meta(object):
        db_table = 'ant'

    name = CharField()
    email = CharField()
    passwd = CharField()
    army = ForeignKeyField(Army, related_name='ants')
