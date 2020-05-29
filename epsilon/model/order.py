# -*- coding:utf-8 -*-

_fields = [
    'tradedate',
    'ordid',
    'bkrid',
    'secid',
    'otype',
    'side',
    'price',
    'qty',
    'poseff',
    'tif',
    'executed',
    'avgexecpx',
    'cnlrequested',
    'cumqty',
    'reqs',
    'rsps'
]


def order2mx(order)
    df = pd.DataFrame(columns=_fields)

    df['tradedate'] = np.array(order.tradedate)
    df['ordid'] = np.array(order.ordid)
    df['bkrid'] = np.array(order.bkrid)
    df['secid'] = np.array(order.secid)
    df['otype'] = np.array(order.otype)
    df['side'] = np.array(order.side)
    df['price'] = np.array(order.price)
    df['qty'] = np.array(order.qty)
    df['poseff'] = np.array(order.poseff)
    df['tif'] = np.array(order.tif)
    df['executed'] = np.array(order.executed)
    df['avgexecpx'] = np.array(order.avgexecpx)
    df['cnlrequested'] = np.array(order.cnlrequested)
    df['cumqty'] = np.array(order.cumqty)
    df['reqs'] = np.array(order.reqs)
    df['rsps'] = np.array(order.rsps)

    return df
