"""This script converts seconds to the appropriate work years, 
weeks, days, hours, and minutes."""

from sys import argv

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_WORKDAY = 8
DAYS_PER_WORKWEEK = 5
HOURS_PER_WORKMONTH = 168
HOURS_PER_WORKYEAR = 2080

SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_WORKDAY = SECONDS_PER_HOUR * HOURS_PER_WORKDAY
SECONDS_PER_WORKWEEK = SECONDS_PER_WORKDAY * DAYS_PER_WORKWEEK
SECONDS_PER_WORKMONTH = SECONDS_PER_HOUR * HOURS_PER_WORKMONTH
SECONDS_PER_WORKYEAR = SECONDS_PER_HOUR * HOURS_PER_WORKYEAR

script, seconds = argv

seconds = int(seconds)
original_seconds = seconds

if seconds >= SECONDS_PER_WORKYEAR:
    years = seconds / SECONDS_PER_WORKYEAR
    seconds -= years * SECONDS_PER_WORKYEAR
else:
    years = 0

if seconds >= SECONDS_PER_WORKMONTH:
    months = seconds / SECONDS_PER_WORKMONTH
    seconds -= months * SECONDS_PER_WORKMONTH
else:
    months = 0

if seconds >= SECONDS_PER_WORKWEEK:
    weeks = seconds / SECONDS_PER_WORKWEEK
    seconds -= weeks * SECONDS_PER_WORKWEEK
else:
    weeks = 0

if seconds >= SECONDS_PER_WORKDAY:
    days = seconds / SECONDS_PER_WORKDAY
    seconds -= days * SECONDS_PER_WORKDAY
else:
    days = 0

if seconds >= SECONDS_PER_HOUR:
    hours = seconds / SECONDS_PER_HOUR
    seconds -= hours * SECONDS_PER_HOUR
else:
    hours = 0

if seconds >= SECONDS_PER_MINUTE:
    minutes = seconds / SECONDS_PER_MINUTE
    seconds -= minutes * SECONDS_PER_MINUTE
else:
    minutes = 0

print "%i years %i months %i weeks %i days %i hours %i minutes %i seconds" % (years, months, weeks, days, hours, minutes, seconds)