# Reddit Timed Poster
# Version 1.0
# Posts threads to reddit at specified time
# Author: /u/Zrob


# Imports
import simplejson
import praw
import time

# Time to wait between checks
INTERVAL = 30

# Numbers into Months
MONTHS = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
			6: "June", 7: "July", 8: "August", 9: "September", 
			10: "October", 11: "November", 12: "December"}

# Submission
class Submission(object):
	def __init__(self, subreddit, username, password, title, link, time):
		self.subreddit = subreddit
		self.username = username
		self.password = password
		self.title = title
		self.link = link
		self.time = time
		self.submit_link = link

	def submit(self):
		submission_title = self.title
		user_agent = "Timed Post 1.0 by /u/Zrob"
		r = praw.Reddit(user_agent=user_agent)
		r.login(self.username, self.password, disable_warning=True)
		submission = r.submit(self.subreddit, submission_title, url=self.submit_link)
		print "Submitted post"
		print "Shortlink: "

	def interval(self, low, high):
		lower_min = low.total_min
		higher_min = high.total_min
		minutes = self.time.total_min

		if lower_min <= higher_min:
			return minutes > lower_min and minutes <= higher_min
		else:
			return minutes > lower_min or minutes <= higher_min


# Time Object
class TimeConverter(object):
	def __init__(self, month, day, hour, minute):
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute
		self.total_min = (self.day * 1440) + (self.hour * 60) + self.minute

	def string_convert(self):
		day_str = str(self.day)
		if self.day < 10:
			day_str = "0" + day_str

		hour_str = str(self.hour)
		if self.hour < 10:
			hour_str = "0" +hour_str

		minute_str = str(self.minute)
		if self.minute < 10:
			minute_str = "0" + minute_str

		return  MONTHS[self.month] + " " + day_str + " at " + hour_str + ":" + minute_str


# Import Data from JSON
s = {}
s = simplejson.load(open("config.json"))
print "Submission data has been loaded"

# Get time to post submission
post_time = TimeConverter(s["time"]["month"], s["time"]["day"],
							s["time"]["hour"], s["time"]["minute"])

# Create the submission
submission = Submission(s["subreddit"], s["username"], s["password"],
							s["title"], s["link"], post_time)

print "Submission planned for " + post_time.string_convert()


# Submission on time
system_time = time.localtime()
previous_time = TimeConverter(system_time.tm_mon, system_time.tm_mday, system_time.tm_hour, system_time.tm_min)
while True:
	system_time = time.localtime()
	current_time = TimeConverter(system_time.tm_mon, system_time.tm_mday, system_time.tm_hour, system_time.tm_min)

	if submission.interval(previous_time, current_time):
		submission.submit()
		break

	print "It's not time to post yet"

	previous_time = current_time
	time.sleep(INTERVAL)
