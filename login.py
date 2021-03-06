from datetime import datetime
import requests


def grab_calendar(uname, pwd, date):
	url = 'https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/EMPL/'
	url2 = 'https://csprd.mcmaster.ca/psc/prcsprd/EMPLOYEE/HRMS_LS/c/SA_LEARNER_SERVICES.SSR_SSENRL_SCHD_W.GBL'

	querystring = {'cmd':'login','languageCd':'ENG'}

	payload = 'ptinstalledlang=ENG&ptlangcd=ENG&ptmode=f&timezoneOffset=300&userid=%s&pwd=%s' % (uname, pwd)

	year = str(date.year)
	month = zero_pad(date.month)
	day = zero_pad(date.day)
	# payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=3&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICXPos=128&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=dXBtIt%2FFP3c%2FgJzz7si8biyde0cMjkZicxvW6m4notI%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT=2016%2F01%2F24&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=7&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICXPos=0&ICYPos=108&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=Ib3m8rCrGfCBQyzIYW0uLlapMv56MlEeyqxoAigXexI%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT=2016%2F03%2F03&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	# payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=8&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL%2489%24&ICXPos=0&ICYPos=667&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=Ib3m8rCrGfCBQyzIYW0uLlapMv56MlEeyqxoAigXexI%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT=2016%2F01%2F27&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=N&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=Y&DERIVED_CLASS_S_SSR_DISP_TITLE=Y&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=N&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	#payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=0&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICXPos=0&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=SNTElR83S%2FraCots88D70wNsYpz%2F%2FZ4ggbDHvFKF7OU%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT=2016%2F02%2F09&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	#payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=8&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL%2489%24&ICXPos=0&ICYPos=667&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=Ib3m8rCrGfCBQyzIYW0uLlapMv56MlEeyqxoAigXexI%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT=2016%2F01%2F27&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=N&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=Y&DERIVED_CLASS_S_SSR_DISP_TITLE=Y&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=N&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	# payload2 = 'ICAJAX=1&ICNAVTYPEDROPDOWN=1&ICType=Panel&ICElementNum=0&ICStateNum=3&ICAction=DERIVED_CLASS_S_SSR_REFRESH_CAL&ICXPos=128&ICYPos=0&ResponsetoDiffFrame=-1&TargetFrameName=None&FacetPath=None&ICFocus=&ICSaveWarningFilter=0&ICChanged=-1&ICResubmit=0&ICSID=dXBtIt%2FFP3c%2FgJzz7si8biyde0cMjkZicxvW6m4notI%3D&ICActionPrompt=false&ICFind=&ICAddCount=&ICAPPCLSDATA=&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$22$=9999&DERIVED_REGFRM1_SSR_SCHED_FORMAT$38$=W&DERIVED_CLASS_S_START_DT='+year+'%2F'+month+'%2F'+day+'&DERIVED_CLASS_S_MEETING_TIME_START=8%3A00AM&DERIVED_CLASS_S_MEETING_TIME_END=10%3A00PM&DERIVED_CLASS_S_SHOW_AM_PM$chk=Y&DERIVED_CLASS_S_SHOW_AM_PM=Y&DERIVED_CLASS_S_MONDAY_LBL$81$$chk=Y&DERIVED_CLASS_S_MONDAY_LBL$81$=Y&DERIVED_CLASS_S_THURSDAY_LBL$chk=Y&DERIVED_CLASS_S_THURSDAY_LBL=Y&DERIVED_CLASS_S_SUNDAY_LBL$chk=Y&DERIVED_CLASS_S_SUNDAY_LBL=Y&DERIVED_CLASS_S_SSR_DISP_TITLE$chk=N&DERIVED_CLASS_S_TUESDAY_LBL$chk=Y&DERIVED_CLASS_S_TUESDAY_LBL=Y&DERIVED_CLASS_S_FRIDAY_LBL$chk=Y&DERIVED_CLASS_S_FRIDAY_LBL=Y&DERIVED_CLASS_S_SHOW_INSTR$chk=N&DERIVED_CLASS_S_WEDNESDAY_LBL$chk=Y&DERIVED_CLASS_S_WEDNESDAY_LBL=Y&DERIVED_CLASS_S_SATURDAY_LBL$chk=Y&DERIVED_CLASS_S_SATURDAY_LBL=Y&DERIVED_SSTSNAV_SSTS_MAIN_GOTO$103$=9999'
	headers = {
		'Host': 'epprd.mcmaster.ca',
		'Connection': 'keep-alive',
		# 'Content-Length': '0',
		'Cache-Control': 'max-age=0',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Origin': 'https://epprd.mcmaster.ca',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.0 Safari/537.36',
		'Content-Type': 'application/x-www-form-urlencoded',
		'Referer': 'https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/EMPL/?cmd=logout',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'en-US,en;q=0.8,ar;q=0.6',
	}

	with requests.Session() as s:
		get_login = s.get('https://epprd.mcmaster.ca/psp/prepprd/?cmd=login', headers=headers)
		response = s.post(url, data=payload, params=querystring, headers=headers)
		cal = s.post(url2, data=payload2, headers=headers)

		with open('data.xml', 'w') as o:
			o.write(cal.text.encode('utf-8'))
		return cal.text


def zero_pad(date):
	if date < 10:
		return '0' + str(date)
	return str(date)
