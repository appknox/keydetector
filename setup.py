from setuptools import find_packages, setup

with open("README.md", "r") as fh:
	description = fh.read()
REQUIREMENTS = [i.strip() for i in open("api_key_detector/requirements.txt").readlines()]

__VERSION__ = "0.0.2"

setup(
	name="ak-keydetector",
	version=__VERSION__,
	author="Appknox Engineering",
	author_email="engineering@appknox.com",
	packages=find_packages(),
    include_package_data=True,
	description="ML Based API Key Detector",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://github.com/appknox/ml-key-detector",
	license='Apache-2.0 license',
	python_requires='>=3.8',
	install_requires=REQUIREMENTS
)
