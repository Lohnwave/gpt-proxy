#
# Copyright (c) all rights reserved
# Author: Lohnwave waveluozu@163.com
# Created on 2024-1-4
#
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]