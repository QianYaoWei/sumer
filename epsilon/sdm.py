# -*- coding:utf-8 -*-
from config import *

_fields = ["tms", "date", "ssid", "bid", "bsz",
            "ask", "asz", "mid", "wmp", "lst",
            "vol", "amt", "oin", "update", "buyVolume",
            "sellVolume", "bidSizeChange", "askSizeChange", "crossBidVolume", "crossAskVolume",
            "vi", "ofi"]


def get_index_by_secid(sdm, secID, tradeIndex=0):
    if tradeIndex >= sdm.sec.length:
        return None

    for i, s in enumerate(sdm.sec[tradeIndex]):
        if secID == s.getSecurityID():
            return i
    return None


def sdm2mx(sdm, secID, tradeIndex=0):
    if tradeIndex >= sdm.daterow.length:
        return None

    start = sdm.daterow[tradeIndex][0]
    end = sdm.daterow[tradeIndex][1]
    secIndex = get_index_by_secid(sdm, secID, tradeIndex)

    df = pd.DataFrame(columns=_fields)

    s = end - start + 1
    df["tms"] = np.array(sdm.tms)

    df["date"] = np.array(sdm.date)

    z = np.zeros(s, dtype=float)
    for i in range(0, s):
        z[i] = sdm.ssid[i + start][secIndex]
    df["ssid"] = z

    for i in range(0, s):
        z[i] = sdm.bid[i + start][secIndex]
    df["bid"] = z

    for i in range(0, s):
        z[i] = sdm.bsz[i + start][secIndex]
    df["bsz"] = z

    for i in range(0, s):
        z[i] = sdm.ask[i + start][secIndex]
    df["ask"] = z

    for i in range(0, s):
        z[i] = sdm.asz[i + start][secIndex]
    df["asz"] = z

    for i in range(0, s):
        z[i] = sdm.mid[i + start][secIndex]
    df["mid"] = z

    for i in range(0, s):
        z[i] = sdm.wmp[i + start][secIndex]
    df["wmp"] = z

    for i in range(0, s):
        z[i] = sdm.lst[i + start][secIndex]
    df["lst"] = z

    for i in range(0, s):
        z[i] = sdm.vol[i + start][secIndex]
    df["vol"] = z

    for i in range(0, s):
        z[i] = sdm.amt[i + start][secIndex]
    df["amt"] = z

    for i in range(0, s):
        z[i] = sdm.oin[i + start][secIndex]
    df["oin"] = z

    for i in range(0, s):
        z[i] = sdm.update[i + start][secIndex]
    df["update"] = z

    for i in range(0, s):
        z[i] = sdm.buyVolume[i + start][secIndex]
    df["buyVolume"] = z

    for i in range(0, s):
        z[i] = sdm.sellVolume[i + start][secIndex]
    df["sellVolume"] = z

    for i in range(0, s):
        z[i] = sdm.bidSizeChange[i + start][secIndex]
    df["bidSizeChange"] = z

    for i in range(0, s):
        z[i] = sdm.askSizeChange[i + start][secIndex]
    df["askSizeChange"] = z

    for i in range(0, s):
        z[i] = sdm.crossBidVolume[i + start][secIndex]
    df["crossBidVolume"] = z

    for i in range(0, s):
        z[i] = sdm.crossAskVolume[i + start][secIndex]
    df["crossAskVolume"] = z

    for i in range(0, s):
        z[i] = sdm.vi[i + start][secIndex]
    df["vi"] = z

    for i in range(0, s):
        z[i] = sdm.ofi[i + start][secIndex]
    df["ofi"] = z

    df.index = df.tms

    return df
