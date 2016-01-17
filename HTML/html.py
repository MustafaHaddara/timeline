# stdlib imports
from datetime import datetime
import sys
sys.path.append('..')

# third party imports
from bs4 import BeautifulSoup

# internal imports
from event import Event

DAYS = []

def get_events(xml_data):
	parsed = BeautifulSoup(xml_data, 'html.parser')

	# only one page
	page = parsed.find_all('page')[0]
	# only one field
	field = None
	for f in parsed.find_all('field'):
		if f['id'] == 'win0divPAGECONTAINER':
			field = f
			break

	cdata = field.contents[0]
	parsed = BeautifulSoup(cdata, 'html.parser')
	# print '\n'*50
	# print parsed
	# sys.exit()
	# print parsed
	table = parsed.find(id='WEEKLY_SCHED_HTMLAREA')
	rows = table.find_all('tr')

	## first row is header
	headers = rows[0].find_all('th')
	for head in headers:
		if 'SSSWEEKLYDAYBACKGROUND' in head['class']:
			texts = head.contents
			day = texts[0]
			date = texts[1].text.strip()
			DAYS.append(day + ' ' + date)


	events = []
	for row in rows:
		cells = row.find_all('td')
		for idx, cell in enumerate(cells):
			sp = cell.find_all('span')
			if len(sp) > 0 and 'SSSTEXTWEEKLY' in sp[0]['class']:
				# print 'day:', DAYS[idx]
				contents = sp[0].contents 
				sub_contents = contents[1].contents
				name = contents[0] + ' ' + sub_contents[0]  # course + lecture
				time = sub_contents[1].contents[0]
				start, end = build_date(time, DAYS[idx])
				print start
				# print end
				location = sub_contents[1].contents[1].text
				e = Event(name, location, start, end)
				events.append(e)

	return events


def build_date(time, day):
	# comes in as string eg. 7:30PM - 10:00PM
	# returns python datetime objects
	dateformat = '%Y %A %b %d %I:%M%p'
	basetime = '2016 ' + day + ' '
	start, end = time.split(' - ')
	start = zero_pad(start)
	end = zero_pad(end)
	# print basetime + start
	starttime = datetime.strptime(basetime + start, dateformat)
	endtime = datetime.strptime(basetime + end, dateformat)
	return starttime, endtime


def zero_pad(time):
	result = ""
	for part in  time.split(':'):
		if len(part) < 2:
			part = '0' + part
		result += part
		result += ':'
	return result[:-1]