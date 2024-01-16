"""  
OUTPUT OF THE PROGRAM IS:
$>python format_ft_time.py | cat -e
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation$
Oct 21 2022$
$>
"""

from datetime import datetime as dt
import time

# Epoch time (POSIX time or UNIX time) is a time from which the computer measures system time.
# In most UNIX versions, the epoch time starts at 00:00:00 UTC on 1 January 1970.
seconds = time.time() #returns the current time in seconds since the epoch
print("Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation".format(seconds, seconds))

date = dt.now()
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
          'Nov', 'Dec']
print(months[date.month - 1], date.day, date.year)

