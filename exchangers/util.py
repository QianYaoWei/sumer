#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime as dt
from .index_def import *
#from .vacations import vacations
#from .shfe import shfe

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
                        type(args[i]) in (int, float):

                    newArgs.append(dt.datetime.fromtimestamp(args[i]))
                else:
                    newArgs.append(args[i])
            print(newArgs)

            f(*newArgs)
        return func


@timestamp2dt
def is_weekend(t):
    if t.weekday() == 5 or t.weekday() == 6:
        return True

    return False


@timestamp2dt(0)
def nearest_time(st, timeStr):
    '''
        st: startTime is instance of datetime.datetime
    '''
    if timeStr[0] == '-':
        t = dt.datetime.combine(st.date(), dt.time.fromtimestamp(timeStr[1:]))
        t -= dt.timedelta(days=1)
    else:
        t = dt.datetime.combine(st.date(), dt.time.fromtimestamp(timeStr[1:]))

    while True:
        if is_vacation(t):
            t -= dt.timedelta(days=1)
        elif is_weekend(t):
            t -= dt.timedelta(days=1)
        else:
            return t

