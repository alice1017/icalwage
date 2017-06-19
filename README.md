# Icalwage - ics to csv

The **icalwage** computes `.ics` file and output `.csv` file.

## usage

```txt
usage: icalwage.py [-h] [-o] [--month MONTH] [--year YEAR] [--from FULL DATE]
                   [--to FULL DATE]
                   ICS FILE CSV FILE

Load calender data from an .ics file, and Output .csv file.

positional arguments:
  ICS FILE          The '.ics' file, this file needed to load work
                    informations.
  CSV FILE          A file name contains csv data.

optional arguments:
  -h, --help        show this help message and exit
  -o, --overwrite   If dest csv file is already exist, overwrite that file.
  --month MONTH     Returns the month data only, use this when ics file is
                    heavy. Please set integer not string. ok: '6' no: 'June'
  --year YEAR       Returns the year data only. Please set christian era. ok:
                    '1989' no: '89'
  --from FULL DATE  If you want to limit the range of a date, use this
                    argument with '--to' arg. Please set full date. ok:
                    '2017.9.1' no: '9.1'
  --to FULL DATE    If you set '--from' argument, please set this argument.
```


