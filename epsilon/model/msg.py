# -*- coding:utf-8 -*-
from config import *

class msg(object):
    @classmethod
    def fields(cls):
        return [
            'ordid',
            'bkrid',
            'text',
            'ostat',
            'poschg',
            'posstat',

            # longchgt;
            # longchgy;
            # shortchgt;
            # shortchgy;

            'fillpx',
            'comm',
            'exordid',

            # index
            'sindex',
            'oindex',
        ]

    @classmethod
    def msg2df(cls, df, msg):
        df['ordid'] = np.array(msg.ordid)
        df['bkrid'] = np.array(msg.bkrid)

        df['text'] = np.array(msg.text)
        df.text = df.text.apply(lambda e: str(e))

        df['ostat'] = np.array(msg.ostat)
        df.ostat = df.ostat.apply(lambda e: chr(e))

        df['poschg'] = np.array(msg.poschg)

        df['posstat'] = np.array(msg.posstat)
        df.posstat = df.posstat.apply(lambda e: chr(e))

        # longchgt;
        # longchgy;
        # shortchgt;
        # shortchgy;

        df['fillpx'] = np.array(msg.fillpx)
        df['comm'] = np.array(msg.comm)
        df['exordid'] = np.array(msg.exordid)
        df.exordid = df.exordid.apply(lambda e: str(e))

        # index
        df['sindex'] = np.array(msg.sindex)
        df['oindex'] = np.array(msg.oindex)

        # if includeQuote is True
        # these fields will be rewriten by quote.quote2df
        # =========================
        df['bid0'] = np.array(msg.bid[0])
        df['bsz0'] = np.array(msg.bsz[0])
        df['ask0'] = np.array(msg.ask[0])
        df['asz0'] = np.array(msg.asz[0])
        df['wmp'] = df.bid0 + (df.ask0 - df.bid0) * df.bsz0 / (df.bsz0 + df.asz0)

        df['tradedate'] = np.array(msg.tradedate)
        df['time'] = np.array(msg.time)
        df['mtype'] = np.array(msg.mtype)
        df.mtype = df.mtype.apply(lambda e: chr(e))

        df['msn'] = np.array(msg.msn)
        # =========================


    @classmethod
    def msg2mx(cls, msg):
        df = pd.DataFrame(columns=cls.fields())
        cls.msg2df(df, msg)
        return df
