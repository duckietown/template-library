
<!-- Note: there is a "branch" in the url -->

![CircleCI](https://circleci.com/gh/duckietown/template-library/tree/v1.svg?style=svg)
[Details.](https://circleci.com/gh/duckietown/template-library/tree/v1)

![codecov](https://codecov.io/gh/duckietown/template-library/branch/v1/graph/badge.svg)


See [details here](https://codecov.io/gh/duckietown/template-library).


# Template for pure Python libraries in Duckietown

This template provides a boilerplate repository for developing Python libraries in Duckietown.

We have the following features:

* Unit-tests using [Nose].
* Building/testing in Docker environment locally.
* Integration with [CircleCI] for automated testing.
* Integration with [CodeCov] for displaying coverage result.
* Integration with [Sphinx] to build code docs. (So far, only built locally.)
* [Jupyter] notebooks, which are run also in CircleCI as tests.
* Version bump using [Bumpversion].
* Code formatting using [Black].
* Command-line program for using the library.

[CodeCov]: https://codecov.io/gh/duckietown
[Sphinx]:  https://www.sphinx-doc.org/en/master/
[Black]: https://github.com/psf/black
[CircleCI]: https://circleci.com/gh/duckietown
[Jupyter]:  https://jupyter.org/
[Bumpversion]: https://github.com/peritus/bumpversion
[Nose]: https://nose.readthedocs.io/en/latest/

## Anatomy of the repo

This repository describes a library called "`duckietown_pondcleaner`" and there is one command-line tool
called `dt-pc-demo.`

*Warning*: Do not remove files/features just because you don't understand. Ask instead.
See: [Chesterson's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence).

### Meta-files

* `.gitignore`: Files ignore by Git.

* `.dtproject`: ...

* `.bumpversion.cfg`: Configuration for bumpversion

* `Makefile`: ...

### Python packaging

* `requirements.txt`: Contains the *pinned* versions of your requirement that
  are used to run tests.

* `MANIFEST.in`: Deselects the tests to be included in the egg.

* `setup.py`: Containes meta information, definition of the scripts, and
  the dependencies information.

### Python code

* `src/` - This is the path that you should set as "sources root" in your tool

* `src/duckietown_pondcleaner`: Contains the code.

* `src/duckietown_pondcleaner/__init__.py`: Contains the `__version__` library.

* `src/duckietown_pondcleaner_tests`: Contains the tests - not included in the egg.

### Docker testing

These are files to build and run a testing container.

* `.dockerignore`: Describes what files go in the docker container.

* `Dockerfile`: ...

### Sphinx

* `src/conf.py`: Sphinx settings

* `src/index.rst`: Sphinx main file

* `src/duckietown_pondcleaner/index.rst`: Documentation for the package


### Coverage

* `.coveragerc`: Options for code coverage.


### Notebooks

* `notebooks`: Notebooks that are run also as a test.

* `notebooks-extra`: Other notebooks (not run as test)

* `notebooks/*.ipynb`: The notebooks themselves.


-----------

-----------


## Cloning/forking/customizing

### Fork this repository

Use the fork button in the top-right corner of the Github page
to fork this template repository.

### Create a new repository

Create a new repository on Github while specifying the newly
forked template repository as a template for your new repository.


### Fill in the blanks

Build a library by following these steps:

- Clone the newly created repository;
- Place your Python packages inside `src/`;
- List the python dependencies in the file `dependencies.txt`;
- Update the appropriate section in the file `setup.py`;

Make sure that there are no other remains:

    grep -r . pondcleaner

Update the branch names in `README.md`.

### Other set up (for admins)

The following are necessary steps for admins to do:

1. Activate on CircleCI. Make one build successful.

2. Activate on CodeCov. Get the `CODECOV_TOKEN`. Put this token in CircleCI environment.

-----------

-----------


## How to use this library



### Test the code

Test the code using Docker by:

    make test-docker

This runs the test using a Docker container built from scratch
with the pinned dependencies in `requirements.txt`.
This is equivalent to what is run on CircleCI.

To run the tests natively, use:

    make test


### Development

We assume you have already setup a Python virtual environment.

Then we suggest you run:

    python setup.py develop

This will install the library in an editable way (rather than copying the sources somewhere else).

If you don't want to install the deps, do:

    python setup.py develop  --no-deps

For example, this is done in the Dockerfile so that
we know we are only using the dependencies in `requirements.txt` with the
exact pinned version.

<!--Run `pip install -U ./` from the repository directory to build and
install the library. To avoid installing a temporary library system-wide,
we suggest you make a temporary directory `dist`, pass the flag `-t ./dist`
to the `pip` command above, this will tell pip to install the library
inside `dist`. You can then use `PYTHON_PATH=./dist python ...` to run a
Python interpreter that will pick up the library installed in `./dist`.--->


### Adding tests

To add another tests, add files with the name `test_*py` in the
package `duckietown_podcleaner_tests`. The name is important.

Tip: make sure that the tests are actually run looking at the coverage results.

### Notes on using the notebooks

Always clean the notebooks before committing them:

    make -C notebooks cleanup

If you don't think you can be diligent, then add the notebooks using Git LFS.

### Releasing a new version

#### Updating the version

The first step is to change the version and tag the repo.
**DO NOT** change the version manually; use the CLI tool `bumpversion` instead.

The tool can be called by:

    make bump    # bump the version, tag the tree

If you need to include the version in a new file, list it inside the file `.bumpversion.cfg` using the
syntax `[bumpversion:file:<FILE_PATH>]`.

#### Releasing the package

The next step is to upload the package to PyPy.
We use [twine]. Invoke using:

    make upload  # upload to PyPy

For this step, uou need to have admin permissions on PyPy.


[twine]: https://pypi.org/project/twine/
