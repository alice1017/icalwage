#!/usr/bin/env python
# coding: utf-8

import os

from datetime import datetime


def adjust_args(args):

    def _get_datetime(query):

        BASIC_ERROR = "Please set full date. ok: '2017.9.1' no: '9.1'"

        fulldate_data = query.split(".")

        if len(fulldate_data) != 3:
            raise TypeError(BASIC_ERROR)

        year, month, day = fulldate_data

        try:
            return datetime(int(year), int(month), int(day))

        except:
            raise TypeError("Incorrect date. " + BASIC_ERROR)

    if args.range_from:

        args.range_from = _get_datetime(args.range_from)

    if args.range_to:

        args.range_to = _get_datetime(args.range_to)

    return args


def check_destfile(destfile, overwrite=False):

    if os.access(destfile, os.F_OK):

        if overwrite:
            return True

        else:
            raise IOError(
                "The dest file is already exist. If you allow overwrite, "
                "use '--overwrite' argument.")

    else:
        return True


def check_sourcefile(sourcefile):

    if not sourcefile.endswith(".ics"):
        raise IOError("The source file is not '.ics' file!")

    else:
        return True
