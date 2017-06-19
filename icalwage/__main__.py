#!/usr/bin/env python
# coding: utf-8

import sys

from .cli import parser


def main(argv=sys.argv):

    if len(argv) == 1:
        parser.parse_args(["-h"])
        sys.exit(1)

    print parser.parse_args()


if __name__ == "__main__":

    main()
