#!/usr/bin/python

# To plot average Safari activity for each day of the week.

# SQLite help from http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys

from os.path import expanduser
home = expanduser("~")
#database = home + "/Library/Safari/History.db"
database = home + "/Desktop/history.db"

con = None

try:
    con = lite.connect(database)

    #cur =  con.cursor()
    #cur.execute('SELECT visit_time FROM history_visits;')

    #data = cur.fetchone()

    #print "%s" % data
    print "Opened database successfully";

except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()