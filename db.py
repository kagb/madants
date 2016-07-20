# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from consts import DB_URI

db = create_engine(DB_URI, echo=True)


def get_session(db=db):
    return sessionmaker(bind=db)
