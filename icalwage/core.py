#!/usr/bin/env python
# coding: utf-8

from StringIO import StringIO
from icalendar import Calendar
from dateutil.relativedelta import relativedelta

DATE_FORMAT = "%Y/%m/%d"
TIME_FORMAT = "%H:%M:%S"


def get_calendar_events(calendar):

    empty_flag = True

    for component in calendar.walk():
        if component.name == "VEVENT":
            empty_flag = False
            yield component

    if empty_flag is True:
        raise SystemError("There are not events in this ics file.")


def compute_calendar_data(rawdata, args):

    print "args.range_from = '{}'".format(args.range_from)
    print "args.range_to = '{}'".format(args.range_to)

    calendar = Calendar.from_ical(rawdata)

    for event in get_calendar_events(calendar):

        if args.


        print event.get("dtstart").dt















