#!/usr/bin/env python
# coding: utf-8

from icalendar import Calendar
from dateutil.relativedelta import relativedelta

DATE_FORMAT = u"%Y/%m/%d"
TIME_FORMAT = u"%H:%M:%S"
WEEKDAYS = [u"月", u"火", u"水", u"木", u"金", u"土", u"日"]


def get_calendar_events(calendar):

    empty_flag = True

    for component in calendar.walk():
        if component.name == "VEVENT":
            empty_flag = False
            yield component

    if empty_flag is True:
        raise SystemError("There are not events in this ics file.")


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

    template = u"{date},{weekday},{start},~,{end},"
    template += u"{hours}時間{minutes}分,{total},{basetime}\n"

    data = {}
    data["date"] = start_dt.strftime(DATE_FORMAT)
    data["weekday"] = WEEKDAYS[start_dt.weekday()]
    data["start"] = start_dt.strftime(TIME_FORMAT)
    data["end"] = end_dt.strftime(TIME_FORMAT)

    time_delta = relativedelta(end_dt, start_dt)
    data["hours"] = time_delta.hours
    data["minutes"] = time_delta.minutes

    decimal_minutes = float(data["minutes"]) / 60
    decimal_totaltime = round((float(data["hours"]) + decimal_minutes), 2)
    data["total"] = decimal_totaltime

    data["basetime"] = round((decimal_totaltime - 0.5), 2)

    return template.format(**data)
