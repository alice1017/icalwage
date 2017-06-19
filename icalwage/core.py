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

    # if empty_flag is True:
    #     raise SystemError("There are not events in this ics file.")


def compute_calendar_data(rawdata, args):

    calendar = Calendar.from_ical(rawdata)
    csv_data = ""

    for event in get_calendar_events(calendar):

        event_start_dt = event.get("dtstart").dt
        event_end_dt = event.get("dtend").dt

        if args.year:

            if event_start_dt.year == args.year:
                csv_data += build_csv_data(event_start_dt, event_end_dt)

        elif args.month:

            if event_start_dt.month == args.month:
                csv_data += build_csv_data(event_start_dt, event_end_dt)

        elif args.range_from and args.range_to:

            if args.range_from < event_start_dt < args.range_to:
                csv_data += build_csv_data(event_start_dt, event_end_dt)

        else:
            csv_data += build_csv_data(event_start_dt, event_end_dt)

    return csv_data


def build_csv_data(start_dt, end_dt):

    print "date: {}".format(start_dt.strftime(DATE_FORMAT))

    return ""
