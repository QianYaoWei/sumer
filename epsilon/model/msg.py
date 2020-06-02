# -*- coding:utf-8 -*-
from config import *

_fields = [
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

def msg2mx(msg):
    df = pd.DataFrame(columns=_fields)

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

    return df
