#!/usr/bin/env python
# coding: utf-8

import sys

from .cli import parser
from .utils import check_destfile


def program(args):

    check_destfile(args.dest, overwrite=args.overwrite)


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(1)

    args = parser.parse_args()

    try:
        status = program(args)
        sys.exit(status)

    except Exception as e:
        error_type = type(e).__name__
        sys.stderr.write("{0}: {1}".format(error_type, e.message))
        sys.exit(1)


if __name__ == "__main__":

    main()
