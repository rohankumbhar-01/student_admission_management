from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in student_admission_management/__init__.py
from student_admission_management import __version__ as version

setup(
	name="student_admission_management",
	version=version,
	description="First Task ",
	author="Rohan_k",
	author_email="rkumbhar@dexciss.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
