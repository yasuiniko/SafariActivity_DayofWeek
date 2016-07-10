# SafariActivity_DayofWeek

Extract activity from `History.db` for OS X/macOS's Safari and plots how active I am on different days of the week.

### Changelog
v0.1	Basic functionality added:
* Finds `History.db` file from `~/Library/Safari/` automatically
* Will catch if the database cannot be opened
* Converts NSDate timestamps for history data into day of the week
	* Note that time zone differences are probably not correct since Safari likely looks to the system to determine the time and travelling users (like me) don't always update this immediately
* Matlibplot histogram works but is ugly

