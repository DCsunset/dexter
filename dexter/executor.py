from typing import List
from functools import partial
import subprocess
import multiprocessing

def run_command(cmd, stdout):
	ret = subprocess.Popen(cmd, text=True, shell=True, stdout=stdout)
	ret.wait()
	return ret.stdout

class Executor:
	"""
	Execute multiple commands concurrently
	"""
	def __init__(self, commands: List[str]):
		self.commands = commands
		self.pool = None
		self.outputs = None
	
	"""
	Run commands in parallel
	"""
	def run(self, collectOutput=True, processes=None):
		if collectOutput:
			stdout = subprocess.PIPE
		else:
			stdout = None

		self.pool = multiprocessing.Pool(processes=processes)
		func = partial(run_command, stdout=stdout)
		self.outputs = self.pool.map_async(func, self.commands)
		
	"""
	Wait for all commands to finish
	"""
	def wait(self) -> List[str]:
		self.outputs.wait()
		return self.outputs.get()
		
	"""
	Kill all commands
	"""
	def kill(self):
		self.pool.terminate()

"""
Run and wait for commands
"""
def run_and_wait(commands: List[str], collectOutput=True) -> List[str]:
	executor = Executor(commands)
	executor.run(collectOutput=collectOutput)
	return executor.wait()
