#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import exchangers
from exchangers import *


@util.timestamp2dt()
def timetest(ut, t1, t2, padding):
    ut.assertEqual(t1, dt.datetime(2019, 1, 30, 18, 45, 24, 439856))
    ut.assertEqual(t2, dt.datetime(2020, 7, 25, 18, 45, 24, 933667))
    ut.assertEqual(padding, "padding")

    pass


class Testutil(unittest.TestCase):

    def test_timestamp2dt(self):
        timetest(self, 1548845124.439856, 1595673924.933667, "padding")

    def test_is_weekend(self):
        self.assertTrue(is_weekend(1595760324))
        self.assertFalse(is_weekend(1595846724))


if __name__ == '__main__':
    unittest.main()

