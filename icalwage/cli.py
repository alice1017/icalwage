#!/usr/bin/env python
# coding: utf-8

from argparse import ArgumentParser

parser = ArgumentParser(
    prog="icalwage.py",
    description="Load a ics file and return csv file")

# POSITIONALS
parser.add_argument(
    "source",
    metavar="ICS FILE",
    action="store",
    help="The '.ics' file, this file needed to load work informations.")

parser.add_argument(
    "dest",
    metavar="CSV FILE",
    action="store",
    help="A file name contains csv data.")

# OPTIONALS
parser.add_argument(
    "-o", "--overwrite",
    dest="overwrite",
    action="store_true",
    help="If dest csv file is already exist, overwrite that file.")

parser.add_argument(
    "--month",
    dest="month",
    action="store",
    help="Returns the month data only, use this when ics file is heavy. "
         "Please set integer not string. ok: '6' no: 'June'")

parser.add_argument(
    "--year",
    dest="year",
    action="store",
    help="Returns the year data only. Please set christian era. "
         "ok: '1989' no: '89'")

parser.add_argument(
    "--from",
    metavar="FULL DATE",
    dest="range_from",
    action="store",
    help="If you want to limit the range of a date, use this argument "
         "with '--to' arg. Please set full date. ok: '2017.9.1' no: '9.1'")

parser.add_argument(
    "--to",
    metavar="FULL DATE",
    dest="range_to",
    action="store",
    help="If you set '--from' argument, please set this argument.")
