# Template: template-library

This template provides a boilerplate repository for developing 
Python libraries in Duckietown.


## How to use it

### 1. Fork this repository

Use the fork button in the top-right corner of the github page 
to fork this template repository.


### 2. Create a new repository

Create a new repository on github.com while specifying the newly 
forked template repository as a template for your new repository.


### 3. Fill in the blanks

Build a library by following these steps:
- Clone the newly created repository;
- Place your Python packages inside `include/`;
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