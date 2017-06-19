#!/usr/bin/env python
# coding: utf-8

import os


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
