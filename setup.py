from setuptools import find_packages, setup

# :==> Fill in your project data here
package_name = '<LIBRARY_NAME>'
library_webpage = '<LIBRARY_WEB_PAGE>'
maintainer = '<YOUR_FULL_NAME>'
maintainer_email = '<YOUR_EMAIL_ADDRESS>'
short_description = '<BRIEF_DESCRIPTION>'
full_description = """
<LONG_DESCRIPTION>
"""

if "<" in package_name:
    msg = "Please fill in the project data in setup.py."
    raise ValueError(msg)


# Read version from the __init__ file
def get_version_from_source(filename):
    import ast
    v = None
    with open(filename) as f:
        for line in f:
            if line.startswith("__version__"):
                v = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError("No version found in %r." % filename)
    if v is None:
        raise ValueError(filename)
    return v


version = get_version_from_source("src/duckietown_pondcleaner/__init__.py")

# read project dependencies
# NO - dependencies.txt is for testing dependiences - EVERYTHING PINNED
# The requirements here must be broad.
# dependencies_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dependencies.txt')
# with open(dependencies_file, 'rt') as fin:
#     dependencies = list(filter(lambda line: not line.startswith('#'), fin.read().splitlines()))

install_requires = []
tests_require = []

# compile description
underline = "=" * (len(package_name) + len(short_description) + 2)
description = """
{name}: {short}
{underline}

{long}
""".format(
    name=package_name,
    short=short_description,
    long=full_description,
    underline=underline,
)

console_scripts = [
    "dt-pc-demo = duckietown_pondcleaner:dt_pc_demo",
]

# setup package
setup(
    name=package_name,
    author=maintainer,
    author_email=maintainer_email,
    url=library_webpage,
    tests_require=tests_require,
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages("./src"),
    long_description=description,
    version=version,
    entry_points={"console_scripts": console_scripts},
)
