# -*- coding:utf-8 -*-
from config import *


_fields = [
    'tradedate',
    'time',
    'mtype',
    'msn',

    # Quote
    'secid',
    'origtime',
    'dfid',
    'qmtype',
    'bid',
    'bsz',
    'ask',
    'asz',
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


def quote2mx(quote):
    df = pd.DataFrame(columns=_fields)

    df['tradedate'] = np.array(quote.tradedate)
    df['time'] = np.array(quote.time)
    df['mtype'] = np.array(quote.mtype)
    df['msn'] = np.array(quote.msn)

    # Quote
    df['secid'] = np.array(quote.secid)
    df['origtime'] = np.array(quote.origtime)
    df['dfid'] = np.array(quote.dfid)
    df['qmtype'] = np.array(quote.qmtype)
    df['bid'] = np.array(quote.bid)
    df['bsz'] = np.array(quote.bsz)
    df['ask'] = np.array(quote.ask)
    df['asz'] = np.array(quote.asz)
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
    return df
