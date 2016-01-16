# Main Class

# stdlib imports
from datetime import datetime, timedelta

# third party imports
# none

# internal imports
import builder
import event

def main():
	base_date = datetime(2016,01,01,10,0,0)
	week_delta = timedelta(days=7)
	hour_delta = timedelta(hours=2)
	current_date = base_date
	events = []
	for i in range(10):
		evt = event.Event(name="test"+str(i), location="loc"+str(i), start=current_date, end=current_date + hour_delta)
		current_date += week_delta
		events.append(evt)

	builder.writeCalendarEvents(events, 'built.ics')

if __name__ == '__main__':
	main()