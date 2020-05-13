# -*- coding:utf-8 -*-
import epsilon
import jpype

if __name__ == "__main__":
    #con = epsilon.db_connection()
    #jpkg = jpype.JPackage("clover.model.matlab")
    #sdm = jpkg.SecurityDataMatrixPT()
    #epsilon.dolphin()
    mx = epsilon.load_json_raw('/root/tests/aa.json', [25899], 1)
    print(mx.size)
    print(mx.columns)
    print(mx)
    
