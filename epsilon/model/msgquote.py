# -*- coding:utf-8 -*-
from config import *
from .quote import quote
from .msg import msg

class msgquote(object):
    @classmethod
    def fields(cls):
        return quote.fields() + msg.fields()

    @classmethod
    def msgquote2mx(cls, mq):
        df = pd.DataFrame(columns=cls.fields())
        msg.msg2df(df, mq)
        quote.quote2df(df, mq)

        return df
