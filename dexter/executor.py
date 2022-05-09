from typing import List
import subprocess

class Executor:
	"""
	Execute multiple commands concurrently
	"""
	def __init__(self, commands: List[str]):
		self.commands = commands
		self.handles = []
	
	"""
	Run commands in parallel
	"""
	def run(self):
		for cmd in self.commands:
			handle = subprocess.Popen(cmd, shell=True)
			self.handles.append(handle)
		
	"""
	Wait for all commands to finish
	"""
	def wait(self):
		for handle in self.handles:
			handle.wait()
		self.handles = []
		
	"""
	Kill all commands
	"""
	def kill(self):
		for handle in self.handles:
			handle.kill()
		self.handles = []

"""
Run and wait for commands
"""
def run_and_wait(commands):
	executor = Executor(commands)
	executor.run()
	executor.wait()
