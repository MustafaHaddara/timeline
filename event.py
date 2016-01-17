# Event.py
# Defines the internal event class

class Event:
	def __init__(self, name, location, start, end):
		self.name = name
		self.location = location
		# dates should be build using the python stdlib module datetime
		self.start = start
		self.end = end

	def pushBy(self, delta):
		new_start = self.start + delta
		new_end = self.end + delta
		return Event(self.name, self.location, new_start, new_end)
