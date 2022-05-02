import time
import datetime

class Metrics:
	def __init__(self) -> None:
		self._totalTime = datetime.timedelta(0) 
		self._count = 0 
		self._expStart = 0 
		self._expEnd = 0
	
	def start(self):
		self._expStart = datetime.datetime.now()

	def end(self):
		self._expEnd = datetime.datetime.now()
		
	
	def timedFuncCall(self, func):
		start = datetime.datetime.now()
		ret = func()
		end = datetime.datetime.now()
		self._totalTime += end - start
		self._count += 1
		return ret

	def getThroughput(self):
		expTimeinSeconds = (self._expEnd - self._expStart).total_seconds()
		return self._count / expTimeinSeconds
	
	def getLatency(self):
		return self._totalTime / self._count

	