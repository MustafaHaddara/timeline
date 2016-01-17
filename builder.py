#!/usr/bin/python

# stdlib imports
# none

# third party imports
from icalendar import Calendar, Event, vText

# internal imports
# none

# Global Vars
PROD_ID = '-//TEST//CALENDAR//2016//EN'

def writeCalendarEvents(events, filename):
	# event:
	#	name: "Test"
	#	start: "2016-01-16-12-0-0"
	#	end: "2016-01-17-12-0-0"
	#	location: jhe
	cal = Calendar()
	cal.add('prodid', PROD_ID)
	cal.add('version', '2.0')

	for event in events:
		iCalEvent = Event()
		iCalEvent.add('dtstart', event.start)
		iCalEvent.add('dtend', event.end)
		iCalEvent.add('summary', vText(event.name))
		iCalEvent.add('location', vText(event.location))

		cal.add_component(iCalEvent)

	print 'Done'
	return cal.to_ical()
