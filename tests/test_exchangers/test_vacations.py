#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from exchangers import *


class Testvacations(unittest.TestCase):

    def test_is_vacation(self):
        # 2020-01-01
        self.assertTrue(vacations.is_vacation(1577808000))

        # 2020-01-02
        self.assertFalse(vacations.is_vacation(1577894400))

        # 2020-04-05
        self.assertTrue(vacations.is_vacation(1586016000))

        # 2020-04-07
        self.assertFalse(vacations.is_vacation(1586188800))


    def test_is_free(self):
        # 2020-04-05
        self.assertTrue(vacations.is_free(1586016000))

        # 2020-07-05
        self.assertTrue(vacations.is_free(1593878400))

        # 2020-07-27 18:45:24
        self.assertFalse(vacations.is_free(1595846724))


    def test_nearest_time(self):
        # 2020-07-06 Mon
        t1 = 1593964800

        # 2020-07-03 21:00:00 Fri
        t2 = 1593781200

        nt = vacations.nearest_time(t1, "-21:00:00")
        self.assertEqual(t2, nt)
        # ============================================

        # 2020-07-03 Fri
        t1 = 1593705600

        # 2020-07-02 21:00:00 Thu
        t2 = 1593694800
        nt = vacations.nearest_time(t1, "-21:00:00")
        self.assertEqual(t2, nt)
        # ============================================
        # 2020-01-02 Thu
        t1 = 1577894400

        # 2019-12-31 21:00:00
        t2 = 1577797200
        nt = vacations.nearest_time(t1, "-21:00:00")
        self.assertEqual(t2, nt)
        # ============================================
        # 2020-10-09 Fri
        t1 = 1602172800

        # 2020-09-30 21:00:00
        t2 = 1601470800
        nt = vacations.nearest_time(t1, "-21:00:00")
        self.assertEqual(t2, nt)


    def test_is_session_skipped(self):
        # 2020-10-09 Fri
        t = 1602172800
        self.assertTrue(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Night, t))

        self.assertFalse(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Morning1, t))

        # 2020-07-02 21:00:00 Thu
        t = 1593694800
        self.assertFalse(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Night, t))

        self.assertFalse(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Morning1, t))

        # 2020-07-05 Sun
        t = 1593878400
        self.assertTrue(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Night, t))

        self.assertTrue(vacations.is_session_skipped(ExchangerID_SHFE,\
                Session_Morning1, t))


    def test_has_vacation_inbetween(self):
        # 2020-07-03 21:00:00 Fri
        t1 = 1593781200

        # 2020-07-06 Mon
        t2 = 1593964800
        self.assertFalse(vacations.has_vacation_inbetween(t1, t2))
        # ============================================
        # 2019-12-31 21:00:00
        t1 = 1577797200

        # 2020-01-02 Thu
        t2 = 1577894400
        self.assertTrue(vacations.has_vacation_inbetween(t1, t2))
        # ============================================
        # 2020-09-30 21:00:00
        t1 = 1601470800

        # 2020-10-09 Fri
        t2 = 1602172800
        self.assertTrue(vacations.has_vacation_inbetween(t1, t2))


if __name__ == '__main__':
    unittest.main()

