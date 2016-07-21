# -*- coding: utf-8 -*-

from peewee import CharField, ForeignKeyField

from models.base import BaseModel


class WebSite(BaseModel):

    domain = 'WebSite'

    name = CharField()
    home = CharField()


class Army(BaseModel):

    domain = 'Army'

    name = CharField()
    website = ForeignKeyField(WebSite, related_name='armies')


class Ant(BaseModel):

    domain = 'Ant'

    name = CharField()
    email = CharField()
    passwd = CharField()
    army = ForeignKeyField(Army, related_name='ants')
