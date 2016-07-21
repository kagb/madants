# -*-coding: utf-8 -*-

import os
import sys

import requests
import cookielib

MADANTS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def init_path():
    if not MADANTS_PATH == sys.path[0]:
        sys.path.insert(0, MADANTS_PATH)


init_path()


def new_session(cookie_file=''):
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename=cookie_file)
    try:
        session.cookies.load(ignore_discard=True)
    except:
        print("Cookie 未能加载")
    return session
