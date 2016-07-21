# -*-coding: utf-8 -*-

import os
import sys

MADANTS_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def init_path():
    if not MADANTS_PATH == sys.path[0]:
        sys.path.insert(0, MADANTS_PATH)


init_path()
