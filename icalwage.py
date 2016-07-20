#!/usr/bin/env python
#coding: utf-8

import os
import sys
import miniparser
from miniparser import kill
from icalendar import Calendar
from dateutil.relativedelta import relativedelta
from StringIO import StringIO

parser = miniparser.parser()
date_format = "%Y/%m/%d"
time_format = "%H:%M:%S"

@parser.option("-s", "--show-event",
        description="Show event list and time. Please set .ics file to arg.")
def show_event(ics_file):
    check_exist_file(ics_file)

    ical = Calendar.from_ical(open(ics_file,"r").read())
    for event in get_events(ical):

        # about time
        start = event.get("dtstart").dt
        end = event.get("dtend").dt
        print start.strftime(date_format), ":",
        print start.strftime(time_format), "~", end.strftime(time_format), ":",

        # about time diff
        delta = relativedelta(end, start)
        print "%d時間" % delta.hours,
        print "%d分"   % delta.minutes

@parser.option("-w", "--work-wage",
        description="Calcuation your wage. Please set ics file and hourly wage",
        argument_types={"ics_file":str, "hourly_wage":int})
def calc_wage(ics_file, hourly_wage):
    check_exist_file(ics_file)

    ical = Calendar.from_ical(open(ics_file,"r").read())

    minutely_wage = hourly_wage/60
    total_wage = 0

    for event in get_events(ical):

        # about time
        start = event.get("dtstart").dt
        end = event.get("dtend").dt
        print start.strftime(date_format), ":",
        print start.strftime(time_format), "~", end.strftime(time_format), ":",

        # about time diff
        delta = relativedelta(end, start)
        total_wage += ((hourly_wage*delta.hours)+(minutely_wage*delta.minutes)) 
        print "%d時間" % delta.hours,
        print ("%d分" if len(str(delta.minutes)) == 2 else "0%d分") % delta.minutes,
        print ":", ((hourly_wage*delta.hours)+(minutely_wage*delta.minutes))
    print "-"*50
    print "総額 :", total_wage

@parser.option("-c", "--csv",
        description="Make CSV file. Please set ics file and file name.")
def make_csv(ics_file, filename):
    check_exist_file(ics_file)

    if os.access(filename, os.F_OK):
        print "fatal: '%s' file is already exist." % filename
        kill(1)

    if filename.endswith(".csv") == False:
        filename = filename+".csv"

    ical = Calendar.from_ical(open(ics_file,"r").read())
    fp = open(filename, "w")
    io = StringIO()
    sys.stdout = io

    put = sys.stdout.write

    for event in get_events(ical):

        # about time
        start = event.get("dtstart").dt
        end = event.get("dtend").dt
        put(start.strftime(date_format) + ",")
        put(start.strftime(time_format) + ",~," + end.strftime(time_format) + ",")

        # about time diff
        delta = relativedelta(end, start)
        put(u"%d時間" % delta.hours)
        put( (u"%d分," if len(str(delta.minutes)) == 2 else u"0%d分,") % delta.minutes )

        # time numberling
        float_min = float(delta.minutes) / 60
        time_num = round(float(delta.hours) + float_min,2)
        put("%g," % time_num)

        # minus 0.5
        put("%g\n" % (round(time_num - 0.5,2)))

    sys.stdout = sys.__stdout__
    fp.write(io.getvalue().encode("SHIFT_JIS"))
    fp.close()

def get_events(calendar):
    for component in calendar.walk():
        if component.name == "VEVENT":
            yield component

def check_exist_file(path):
    if os.access(path, os.F_OK):
        return True
    else:
        print "fatal: file not found."
        kill(1)

if __name__ == "__main__":
    parser.parse()
