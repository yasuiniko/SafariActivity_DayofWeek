#!/usr/bin/python

# To plot average Safari activity for each day of the week.


import sqlite3 as lite
import numpy as np
import pylab as pl
import sys
import datetime

# Find the Safari history database which is in ~/Library/Safari/ by default
from os.path import expanduser
home = expanduser("~")
database = home + "/Library/Safari/History.db"

# Try to open the database
# SQLite help from http://zetcode.com/db/sqlitepythontutorial/
con = None

try:

    # For Testing
    #print "Opened database successfully";

    con = lite.connect(database)
    cur =  con.cursor()
    
    cur.execute('SELECT visit_time FROM history_visits;')

    data = [int(data[0]) for data in cur.fetchall()]
    # Convert visit_time from NSDate format to UNIX time
    data = map(lambda x: x + 978307200, data)
    data = np.asarray(data, 'datetime64[s]')
    data = data.tolist()

    # Find the day of week where 0 is Monday and 6 is Sunday
    dow = map(lambda x: x.weekday(), data)

    # Plot a histogram of the results
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pl.hist(dow, bins = [0,1,2,3,4,5,6,7], align = "left")
    pl.xlabel('Day of Week')
    pl.xticks([0,1,2,3,4,5,6,7], names, size = "small")
    pl.ylabel('Number of Websites Visited')
    pl.show()

    # To split analysis up into weeks, check for when a value is less than the previous.

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()