#!/usr/bin/env python
# coding: utf-8

import pytz
import unittest
import datetime

from icalwage.cli import parser
from icalwage.utils import (
    adjust_args,
    check_destfile,
    check_sourcefile,
    _get_datetime
)


class IcalwageTester(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        pass

    def test_adjust(self):

        with self.assertRaises(SystemError):
            args = parser.parse_args(
                [
                    "--year", "1989", "--month", "6",
                    "work.ics", "dest.csv"
                ])
            adjust_args(args)

    def test_adjust2(self):

        with self.assertRaises(SystemError):
            args = parser.parse_args(
                ["--from", "2017.1.1", "work.ics", "dest.csv"])
            adjust_args(args)

    def test_adjust3(self):

        with self.assertRaises(TypeError):
            args = parser.parse_args(
                ["--year", "year", "work.ics", "dest.csv"])
            adjust_args(args)

    def test_adjust4(self):

        with self.assertRaises(TypeError):
            args = parser.parse_args(
                ["--month", "June", "work.ics", "dest.csv"])
            adjust_args(args)

    def test_destfile(self):

        with self.assertRaises(IOError):
            check_destfile("work.ics")

    def test_destfile2(self):

        self.assertTrue(check_destfile("work.ics", overwrite=True))

    def test_sourcefile(self):

        with self.assertRaises(IOError):
            check_sourcefile("source")

    def test_makedtobj(self):

        with self.assertRaises(TypeError):
            _get_datetime("2017")

    def test_makedtobj2(self):

        with self.assertRaises(TypeError):
            _get_datetime("query")

    def test_makedtobj3(self):

        self.assertEqual(
            _get_datetime("2017.1.1"),
            datetime.datetime(
                2017, 1, 1, tzinfo=pytz.timezone("Asia/Tokyo"))
        )

if __name__ == '__main__':

    unittest.main(verbosity=2)
