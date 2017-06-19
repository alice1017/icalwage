#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
from icalwage import __author__, __version__

setup(
    name="icalwage",
    author=__author__,
    version=__version__,
    license="MIT License",
    url="https://github.com/alice1017/icalwage",
    description="The icalwage computes the iCal calendar and output csv file.",
    install_requires=["icalendar", "python-dateutil"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "icalwage=icalwage.__main__:main"
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2"
    ]
)
