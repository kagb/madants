# -*- coding: utf-8 -*-

import arrow

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Model(Base):
    id = Column(Integer, primary_key=True)
    create_time = Column(DateTime, default=arrow.now().naive)


class Ant(Model):

    domain = 'Ant'

    name = Column(String)
    email = Column(String)
    passwd = Column(String)
    website_id = Column(Integer)
    refer_id = Column(Integer)


class WebSite(Model):

    domain = 'WebSite'

    name = Column(String)
