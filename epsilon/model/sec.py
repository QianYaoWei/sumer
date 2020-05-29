# -*- coding:utf-8 -*-

_fields = [
    'secid',
    'sectype',
    'exchange',
    'symbol',
    'mmy',
    'multiplier',
    'minpxincr',
    'oindex'
]


def sec2mx(sec):
    df = pd.DataFrame(columns=_fields)

    df['secid'] = np.array(sec.secid)
    df['sectype'] = np.array(sec.sectype)
    df['exchange'] = np.array(sec.exchange)
    df['symbol'] = np.array(sec.symbol)
    df['mmy'] = np.array(sec.mmy)
    df['multiplier'] = np.array(sec.multiplier)
    df['minpxincr'] = np.array(sec.minpxincr)
    df['oindex'] = np.array(sec.oindex)
    return df

