import datetime
import numpy as np
import matplotlib.pyplot as plt # convention
import os
import sqlite3 as lite
import sys


if __name__ == '__main__':
    home = os.path.expanduser('~')
    database = os.path.join(home, "Library/Safari/History.db")
    print(database)
    # idk how to use SQL so...
    con = lite.connect(database)
    cur =  con.cursor()
    cur.execute('SELECT visit_time FROM history_visits;')

    # grabs the first index of every 'data' in 
    # cur.fetchall() and converts it to an int,
    # then puts it in a list. equivalent to:
    # data = list(map(lambda x: int(x[0]), cur.fetchall()))
    data = [int(data[0]) for data in cur.fetchall()]

    """
    # Convert visit_time from NSDate format to UNIX time
    # adds big constant to each item in data.
    # used to return a list, but now returns a map 
    # object, which is basically a list you can only
    # look at once.
    data = map(lambda x: x + 978307200, data)
    """

    # actually we have to make it a list so we can 
    # put it into a numpy array
    data = list(map(lambda x: x + 978307200, data))

    # convert to numpy array so we can extract some
    # time data that isn't "seconds since epoch"
    data = np.asarray(data, 'datetime64[s]').tolist()

    # Find the day of week where 0 is Monday and 6 is Sunday
    day_of_week = list(map(lambda x: x.weekday(), data))

    # total number of data points
    total = len(day_of_week)
    # number in a given day i (finds length of list of 
    # data which are only from day i)
    num_in_day = lambda i: len(list(filter(lambda x: x == i, day_of_week)))
    
    # find num in each day from 0 to 6
    counts = list(map(num_in_day, range(7)))

    # get percent
    data = [count/total*100 for count in counts]

    # plot data
    names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.bar(left=list(map(lambda x: x-0.5, range(7))), height=data)
    plt.xlabel('Day of Week')
    plt.xticks(list(range(8)), names, size='small')
    plt.ylabel('Percent of All Activity')
    plt.show()

    con.close()



