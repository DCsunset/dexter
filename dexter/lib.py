from pathlib import Path
import os

class Logger:
	def __init__(self, filename) -> None:
		# create parent directory if it doesn't exist
		dirname = os.path.dirname(filename)
		Path(dirname).mkdir(parents=True, exist_ok=True)
		self.f = open(filename, "w+")
	
	def __del__(self):
		self.close()

	def append(self,data):
		self.f.write(data)

	def close(self):
		self.f.close()	
	

    