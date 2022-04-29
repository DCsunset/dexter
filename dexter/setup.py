from setuptools import setup
from os import path

version = "0.1.0"

repo_base_dir = path.abspath(path.dirname(__file__))
readme = path.join(repo_base_dir, "README.md")
with open(readme) as f:
	long_description = f.read()

setup(
	name="dexter",
	version=version,
	description="Laboratory assistant"
)
