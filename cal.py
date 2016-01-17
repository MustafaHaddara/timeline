# Main Class

# stdlib imports
from datetime import datetime, timedelta
import sys
import os

# third party imports
# none

# internal imports
import builder
import event
import html
import login

def build_cal(uname, pwd):
	events = get_events(uname, pwd)
	return builder.writeCalendarEvents(events, 'built.ics')

def get_events(uname, pwd):
	time_delta = timedelta(days=7)  # 1 week
	time_current = datetime(2016,1,4,0,0,0) # start on jan 4th, first monday in january
	time_end = datetime(2016,2,1,0,0,0) # beginning of may
	events = []
	xml_resp = login.grab_calendar(uname, pwd, time_current)
	raw_events = html.get_events(xml_resp)
	for event in raw_events:
		for i in range(-1, 12):
			if i == 0:
				events.append(event)
				continue;
			if i != 5:
				new_evt = event.pushBy(i*time_delta)
				events.append(new_evt)

	return events

if __name__ == '__main__':
	main()
