import os
from setuptools import setup, find_packages

# :==> Fill in your project data here
library_name = '<LIBRARY_NAME>'
library_webpage = '<LIBRARY_WEB_PAGE>'
maintainer = '<YOUR_FULL_NAME>'
maintainer_email = '<YOUR_EMAIL_ADDRESS>'
short_description = '<BRIEF_DESCRIPTION>'
full_description = """
<LONG_DESCRIPTION>
"""
# <==: Fill in your project data here

# read project details
dt_project_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.dtproject')
with open(dt_project_file, 'rt') as fin:
    project = dict(map(lambda line: line.split('='), fin.read().splitlines()))
version = project['VERSION']

# read project dependencies
dependencies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dependencies.txt')
with open(dependencies_file, 'rt') as fin:
    dependencies = list(filter(lambda line: not line.startswith('#'), fin.read().splitlines()))

# compile description
description = """
{name}: {short}
=======================================================
{long}
""".format(name=library_name, short=short_description, long=full_description)

# setup package
setup(
    name=library_name,
    author=maintainer,
    author_email=maintainer_email,
    url=library_webpage,
    install_requires=dependencies,
    package_dir={"": "include"},
    packages=find_packages('./include'),
    long_description=description,
    version=version
)
