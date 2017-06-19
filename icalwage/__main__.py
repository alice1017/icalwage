#!/usr/bin/env python
# coding: utf-8

import sys
import codecs

from .cli import parser
from .core import compute_calendar_data
from .utils import (
    adjust_args,
    check_destfile,
    check_sourcefile
)


def program(args):

    args = adjust_args(args)
    check_sourcefile(args.source)
    check_destfile(args.dest, overwrite=args.overwrite)

    with open(args.source, "r") as sfp:

        context = sfp.read()

    with codecs.open(args.dest, "w", "shift_jis") as dfp:

        csv_data = compute_calendar_data(context, args)
        dfp.write(csv_data)

    print "Created {}".format(args.dest)
    return 0


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(1)

    args = parser.parse_args()

    # try:
    status = program(args)
    sys.exit(status)

    # except Exception as e:
    #     error_type = type(e).__name__
    #     sys.stderr.write("{0}: {1}\n".format(error_type, e.message))
    #     sys.exit(1)


if __name__ == "__main__":

    main()
