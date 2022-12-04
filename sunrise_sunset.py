#!/usr/bin/env python
import ephem
import datetime

# define the calc_time function using ephem to do the leg work

def calc_time(year, month, day, lat, long, rise, time):
    eo = ephem.Observer()
    eo.lat, eo.long, eo.date = lat, long, datetime.date(year, month, day)
    sun = ephem.Sun(eo)
    if rise: 
      phase = eo.next_rising
    else:
      phase = eo.next_setting
    return ephem.Date(phase(sun, start=eo.date) + time*ephem.hour).datetime().strftime('%H:%M')

# end def

# get the current date and time in utc
ct = datetime.datetime.utcnow()

# This is the lat/long of the location you want, this is set for Tamworth UK , change it to your lat/long

lat = "52.616667"
long = "-1.683333"

# call the calc_time function with params twice, once for sunrise ( where rise arg == True ) and once for sunset ( with rise arg == False )

print(calc_time(ct.year, ct.month, ct.day, lat, long, True, 0))
print(calc_time(ct.year, ct.month, ct.day, lat, long, False, 0))
