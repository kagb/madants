# -*- coding: utf-8 -*-

from sqlalchemy import create_engine

from consts import DB_URI

db = create_engine(DB_URI, echo=True)
