
<!-- Note: there is a "branch" in the url -->

![CircleCI](https://circleci.com/gh/duckietown/template-library/tree/more.svg?style=svg)
[Details.](https://circleci.com/gh/duckietown/template-library/tree/more)

![codecov](https://codecov.io/gh/duckietown/template-library/branch/more/graph/badge.svg) 
See [details here](https://codecov.io/gh/duckietown/template-library). 
 

# Template for pure Python libraries in Duckietown

This template provides a boilerplate repository for developing Python libraries in Duckietown.

We have the following features:

* Unit-tests using [Nose].
* Building/testing in Docker environment locally.
* Integration with [CircleCI] for automated testing.
* Integration with [CodeCov] for displaying coverage result.
* Integration with [Sphinx] to build code docs. (So far, only built locally)
* [Jupyter] notebooks, which are run also in CircleCI as tests.
* Version bump using [Bumpversion].
* Code formatting using [Black].
* Command-line program for using the library.


[Black]: https://github.com/psf/black
[CircleCI]: https://circleci.com/gh/duckietown
[Jupyter]:  https://jupyter.org/
[Bumpversion]: https://github.com/peritus/bumpversion
[Nose]: https://nose.readthedocs.io/en/latest/

## Anatomy of the repo


The fake library is called "`duckietown_pondcleaner`" and there is one command-line tool
called `dt-pc-demo.`

*Warning*: Do not remove files/features just because you don't understand. Ask instead.
See: [Chesterson's fence](https://en.wikipedia.org/wiki/Wikipedia:Chesterton%27s_fence).

### Meta-files

* `.gitignore`: Files ignore by Git.

* `.dtproject`: ...

* `.bumpversion.cfg`: Configuration for bumpversion

* `Makefile`:

### Python packaging

* `requirements.txt`: Contains the *pinned* versions of your requirement that
  are used to run tests. 
   
* `MANIFEST.in`:
 
* `setup.py`: Containes meta information, definition of the scripts, and 
  the dependencies information.   

### Python code

* `src/`

* `src/duckietown_pondcleaner`

### Docker testing

These are files to build and run a testing container.

* `.dockerignore`: Describes what files go in the docker container.

* `Dockerfile`: ...

### Sphinx

### Coverage

* `.coveragerc`: 



## How to use it

### 1. Fork this repository

Use the fork button in the top-right corner of the Github page 
to fork this template repository.

### 2. Create a new repository

Create a new repository on Github while specifying the newly 
forked template repository as a template for your new repository.


### 3. Fill in the blanks

Build a library by following these steps:

- Clone the newly created repository;
- Place your Python packages inside `src/`;
- List the python dependencies in the file `dependencies.txt`;
- Update the appropriate section in the file `setup.py`;


### 4. Build it!

Run `pip install -U ./` from the repository directory to build and
install the library. To avoid installing a temporary library system-wide,
we suggest you make a temporary directory `dist`, pass the flag `-t ./dist`
to the `pip` command above, this will tell pip to install the library 
inside `dist`. You can then use `PYTHON_PATH=./dist python ...` to run a 
Python interpreter that will pick up the library installed in `./dist`.


### 5. Release a new version

**DO NOT** change the version manually in your files, use the 
CLI tool `bumpversion` instead. If you need to include the version
in a new file, list it inside the file `.bumpversion.cfg` using the
syntax `[bumpversion:file:<FILE_PATH>]`.




# Setting up

* Activate on CircleCI. Make one build successful.
* Activate on CodeCov. Get the CODECOV_TOKEN. Put this token in CircleCI environment. 
