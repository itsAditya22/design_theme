from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in design_theme/__init__.py
from design_theme import __version__ as version

setup(
	name="design_theme",
	version=version,
	description="made for create new UI/theme for frappe",
	author="Aditya Pawar",
	author_email="adityapawar.powerit@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
