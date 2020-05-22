# -*- coding:utf-8 -*-
from config import *
import os
import jpype

from .db import db_connection, dolphin, md_reader, TimeRange, get_quote_db

from .security import qtlist2mx, fetch_qtlist, fetch_qtlist_file, get_sec_objs


if not jpype.isJVMStarted():
    if not os.path.isfile(JVMPath):
        logger.error('java path invalide!')
    args = [JVMArgs, ]

    if JavaPkg:
        args.append('-Djava.class.path=' + ':'.join(JavaPkg))
    jpype.startJVM(JVMPath, *args, convertStrings=False)


def test_utils():
    return jpype.JPackage('clover.epsilon.util').TestUtils
