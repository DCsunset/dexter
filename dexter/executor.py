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
	def run(self, collectOutput=True):
		if collectOutput:
			stdout = subprocess.PIPE
		else:
			stdout = None
		for cmd in self.commands:
			handle = subprocess.Popen(cmd, text=True, shell=True, stdout=stdout)
			self.handles.append(handle)
		
	"""
	Wait for all commands to finish
	"""
	def wait(self) -> List[str]:
		outputs = []
		for handle in self.handles:
			output = handle.communicate()[0]
			outputs.append(output)
		self.handles = []
		return outputs
		
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
def run_and_wait(commands: List[str], collectOutput=True) -> List[str]:
	executor = Executor(commands)
	executor.run(collectOutput=collectOutput)
	return executor.wait()
