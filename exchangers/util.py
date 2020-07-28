#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime as dt
from .index_def import *

class timestamp2dt(object):
    def __init__(self, tpos=-1):
        '''
            decorator
            tpos: specify the position of timestamp, 
                    -1 means all the arguments are timestamp
        '''
        self._tpos = tpos


    def __call__(self, f):
        def func(*args):
            newArgs = []
            for i in range(len(args)):
                if (i == self._tpos or self._tpos == -1) and \
                        args is not object and \
                        type(args[i]) in (int, float):

                    newArgs.append(dt.datetime.fromtimestamp(args[i]))
                else:
                    newArgs.append(args[i])

            return f(*newArgs)
        return func


@timestamp2dt()
def is_weekend(t):
    if t.weekday() == 5 or t.weekday() == 6:
        return True

    return False
