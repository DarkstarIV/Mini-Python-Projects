import datetime

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date:  = %s/%s/%s" % (e.month, e.day, e.year))

print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))