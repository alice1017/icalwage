#!/usr/bin/env python
# coding: utf-8

import sys

from .cli import parser
from .utils import check_destfile


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(1)

    args = parser.parse_args()
    check_destfile(args.dest, overwrite=args.overwrite)


if __name__ == "__main__":

    main()
