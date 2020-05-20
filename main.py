# -*- coding:utf-8 -*-
import epsilon
import jpype
import numpy as np
import pandas as pd
import plot


#qt = epsilon.fetch_qtlist_file('/root/tests/aa.json', [25899])
#mx = epsilon.qtlist2mx(qt, 1)

tu = epsilon.test_utils()
tu.conn()
reader = tu.createJsonQuoteCMDReader("/market_data/json_raw_cn_fut");
qt = epsilon.fetch_qtlist(reader, [26005], '2020-05-18')
mx = epsilon.qtlist2mx(qt, 1)

#con = epsilon.db_connection()
#jpkg = jpype.JPackage("clover.model.matlab")
#sdm = jpkg.SecurityDataMatrixPT()
#epsilon.dolphin()
#print(mx.size)
#print(mx.columns)
#print(mx)
#
