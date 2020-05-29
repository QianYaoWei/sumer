# -*- coding:utf-8 -*-

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
    df['ostat'] = np.array(msg.ostat)
    df['poschg'] = np.array(msg.poschg)
    df['posstat'] = np.array(msg.posstat)

    # longchgt;
    # longchgy;
    # shortchgt;
    # shortchgy;

    df['fillpx'] = np.array(msg.fillpx)
    df['comm'] = np.array(msg.comm)
    df['exordid'] = np.array(msg.exordid)

    # index
    df['sindex'] = np.array(msg.sindex)
    df['oindex'] = np.array(msg.oindex)

    return df
