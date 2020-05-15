# -*- coding:utf-8 -*-
import epsilon
import jpype
import numpy as np
import pandas as pd
import plot


# mx2 = pd.DataFrame(np.arange(10).reshape(5, 2),  columns=['a', 'b'])
#mx = epsilon.load_json_raw('/root/tests/MD_CN_FUT_20200430.json', [25899], 5)
mx = epsilon.load_json_raw('/root/tests/aa.json', [25899], 5)
# mx = epsilon.load_json_raw('/root/tests/jj.json', [25899], 5)

#con = epsilon.db_connection()
#jpkg = jpype.JPackage("clover.model.matlab")
#sdm = jpkg.SecurityDataMatrixPT()
#epsilon.dolphin()
#print(mx.size)
#print(mx.columns)
#print(mx)
#
