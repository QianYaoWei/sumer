# -*- coding:utf-8 -*-
from config import *
import os



if not jpype.isJVMStarted():
    if not os.path.isfile(JVMPath):
        logger.error('java path invalide!')
    args = [JVMArgs, ]

    if JavaPkg:
        args.append('-Djava.class.path=' + ':'.join(JavaPkg))
    jpype.startJVM(JVMPath, *args, convertStrings=False)


def test_utils():
    return jpype.JPackage('clover.epsilon.util').TestUtils
