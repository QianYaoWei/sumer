# -*- coding:utf-8 -*-
from config import *


class order(object):
    @classmethod
    def fields(cls):
        return [
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

    @classmethod
    def order2mx(cls, order):
        df = pd.DataFrame(columns=cls.fields())

        df['tradedate'] = np.array(order.tradedate)
        df['ordid'] = np.array(order.ordid)
        df['bkrid'] = np.array(order.bkrid)
        df['secid'] = np.array(order.secid)

        df['otype'] = np.array(order.otype)
        df.otype = df.otype.apply(lambda e: str(e))

        df['side'] = np.array(order.side)
        df['price'] = np.array(order.price)
        df['qty'] = np.array(order.qty)

        df['poseff'] = np.array(order.poseff)
        df.poseff = df.poseff.apply(lambda e: chr(e))

        df['tif'] = np.array(order.tif)
        df.tif = df.tif.apply(lambda e: chr(e))

        df['executed'] = np.array(order.executed)
        df['avgexecpx'] = np.array(order.avgexecpx)
        df['cnlrequested'] = np.array(order.cnlrequested)
        df['cumqty'] = np.array(order.cumqty)
        df['reqs'] = np.array(order.reqs)
        df['rsps'] = np.array(order.rsps)

        return df
