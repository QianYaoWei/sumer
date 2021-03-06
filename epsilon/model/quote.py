# -*- coding:utf-8 -*-
from config import *

class quote(object):
    @classmethod
    def fields(cls):
        return [
            'tradedate',
            'time',
            'mtype',
            'msn',

            # Quote
            'secid',
            'origtime',
            'dfid',
            'qmtype',
            'bid0',
            'bsz0',
            'ask0',
            'asz0',
            'lastpx',
            'lastsz',
            'lastamt',
            'oin',
            'ttvol',
            'ttamt',

            # Quote - custom
            'buyvol',
            'sellvol',
            'crxbidvol',
            'crxaskvol',
            'bszchg',
            'aszchg'
        ]


    @classmethod
    def quote2df(cls, df, quote):
        df['tradedate'] = np.array(quote.tradedate)
        df['time'] = np.array(quote.time)
        df['mtype'] = np.array(quote.mtype)
        df['msn'] = np.array(quote.msn)

        # Quote
        df['secid'] = np.array(quote.secid)
        df['origtime'] = np.array(quote.origtime)
        df['dfid'] = np.array(quote.dfid)
        df['qmtype'] = np.array(quote.qmtype)
        df.qmtype = df.qmtype.apply(lambda e: chr(e))


        df['bid0'] = np.array(quote.bid[0])
        df['bsz0'] = np.array(quote.bsz[0])
        df['ask0'] = np.array(quote.ask[0])
        df['asz0'] = np.array(quote.asz[0])
        df['wmp'] = df.bid0 + (df.ask0 - df.bid0) * df.bsz0 / (df.bsz0 + df.asz0)

        df['lastpx'] = np.array(quote.lastpx)
        df['lastsz'] = np.array(quote.lastsz)
        df['lastamt'] = np.array(quote.lastamt)
        df['oin'] = np.array(quote.oin)
        df['ttvol'] = np.array(quote.ttvol)
        df['ttamt'] = np.array(quote.ttamt)

        # Quote - custom
        df['buyvol'] = np.array(quote.buyvol)
        df['sellvol'] = np.array(quote.sellvol)
        df['crxbidvol'] = np.array(quote.crxbidvol)
        df['crxaskvol'] = np.array(quote.crxaskvol)
        df['bszchg'] = np.array(quote.bszchg)
        df['aszchg'] = np.array(quote.aszchg)


    @classmethod
    def quote2mx(cls, quote):
        df = pd.DataFrame(columns=cls.fields())
        quote2df(df, quote)
        return df
