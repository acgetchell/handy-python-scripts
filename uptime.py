"""This script converts minutes to the appropriate weeks, days, hours,
and minutes and also calculates yearly uptime."""

from sys import argv

MINUTES_PER_YEAR = 525949
MINUTES_PER_WEEK = 10080
MINUTES_PER_DAY = 1440
MINUTES_PER_HOUR = 60

script, minutes = argv

minutes = int(minutes)
original_minutes = minutes

if minutes > MINUTES_PER_WEEK:
    weeks = minutes / MINUTES_PER_WEEK
    minutes -= weeks * MINUTES_PER_WEEK
else:
    weeks = 0

print minutes

if minutes > MINUTES_PER_DAY:
    days = minutes / MINUTES_PER_DAY
    minutes -= days * MINUTES_PER_DAY
else:
    days = 0

print minutes

if minutes > MINUTES_PER_HOUR:
    hours = minutes / MINUTES_PER_HOUR
    minutes -= hours * MINUTES_PER_HOUR
else:
    hours = 0

print "%i weeks %i days %i hours %i minutes" % (weeks, days, hours, minutes)
print "If you entered total downtime per year in minutes, that's an uptime of \
    %i%%" % ((float(MINUTES_PER_YEAR - original_minutes)
            /float(MINUTES_PER_YEAR)*100))
