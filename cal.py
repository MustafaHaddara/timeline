# Main Class

# stdlib imports
from datetime import datetime, timedelta
import sys
import os
sys.path.append('~/timeline')
#sys.path.append(os.path.abspath('Cal')
#sys.path.append('HTML')
#sys.path.append('Mosaic')

# third party imports
# none

# internal imports
import builder
import event
import html
import login

def build_cal(uname, pwd):
	events = get_events(uname, pwd)
	builder.writeCalendarEvents(events, 'built.ics')

def get_events(uname, pwd):
	time_delta = timedelta(days=7)  # 1 week
	time_current = datetime(2016,1,4,0,0,0) # start on jan 4th, first monday in january
	time_end = datetime(2016,2,1,0,0,0) # beginning of may
	events = []
	while (time_current < time_end):
		print time_current
		xml_resp = login.grab_calendar(uname, pwd, time_current)
		events = events + html.get_events(xml_resp)
		time_current += time_delta
		break

	print events
	return events

if __name__ == '__main__':
	main()
