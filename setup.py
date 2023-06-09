from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hrpro_mena/__init__.py
from hrpro_mena import __version__ as version

setup(
	name="hrpro_mena",
	version=version,
	description="HRPRO MENA",
	author="TEAMPRO",
	author_email="mohamedshajith.j@groupteampro.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
