#!/usr/bin/env python
#coding: utf-8

from distutils.core import setup

setup(
	name = "icalwage",
	author = "alice1017",
	version = "1.0.0",
    license = "MIT",
    url = "https://github.com/alice1017/icalwage",
	description = "This is the script to calculate the wage from ics file that write out from iCal",
    long_description = open("README.rst").read(),
    install_requires = ["icalendar"],
	scripts = ['icalwage.py']
)

