# -*- coding:utf-8 -*-
from config import *

class sec(object):
    @classmethod
    def fields(cls):
        return [
            'secid',
            'sectype',
            'exchange',
            'symbol',
            'mmy',
            'multiplier',
            'minpxincr',
            'oindex'
        ]

    @classmethod
    def sec2mx(cls, sec):
        df = pd.DataFrame(columns=cls.fields())

        df['secid'] = np.array(sec.secid)
        df['sectype'] = np.array(sec.sectype)
        df.sectype = df.sectype.apply(lambda e: str(e))

        df['exchange'] = np.array(sec.exchange)
        df.exchange = df.exchange.apply(lambda e: str(e))

        df['symbol'] = np.array(sec.symbol)
        df.symbol = df.symbol.apply(lambda e: str(e))

        df['mmy'] = np.array(sec.mmy)
        df.mmy = df.mmy.apply(lambda e: str(e))

        df['multiplier'] = np.array(sec.multiplier)
        df['minpxincr'] = np.array(sec.minpxincr)
        df['oindex'] = np.array(sec.oindex)
        return df

