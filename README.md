# sandbox
This is just a Sandbox.


# Virtual environment setup with Pyenv and Poetry

Requirements:
- [pyenv](https://github.com/pyenv/pyenv#installation), for Python versions management
- [poetry](https://python-poetry.org/docs/#installation), for packaging and dependency management

1. Define the python version with `pyenv`, e.g.:
```bash
pyenv local 3.11
```
so that it also creates a `.python-version` file in the project root.


2. Create an env variable from the file.
 ```bash
 export POETRY_PYTHON_VERSION=$(cat .python-version)
 ```
 
3. Set `pyproject_template.toml` to use `python = "^${POETRY_PYTHON_VERSION"`.

4. Fill the template with the chosen python versions using the following command,
```bash
sed "s/python = \"^\${POETRY_PYTHON_VERSION}\"/python = \"^$POETRY_PYTHON_VERSION\"/" pyproject_template.toml > pyproject.toml
```
note that it directs the output to create or overwrite the file `pyproject.toml`.

5. Double check with `pyenv versions` that the correct version is active. Then force poetry to use this version:
```bash
poetry env use python
```
this already creates the poetry venv, but it doesn't install anything yet. 
You can debug with `poetry debug info` and sanity check that the System will show pyenv path and version as desired, and this should match the virtual environment. Poetry Python version does not need to match it.
```shell
$ poetry debug info

Poetry
Version: 1.7.1
Python:  3.12.0

Virtualenv
Python:         3.11.6
Implementation: CPython
Path:           ~/.cache/pypoetry/virtualenvs/sandbox-py3.11
Executable:     ~/.cache/pypoetry/virtualenvs/sandbox-py3.11/bin/python
Valid:          True

System
Platform:   linux
OS:         posix
Python:     3.11.6
Path:       ~/.pyenv/versions/3.11.6
Executable: ~/.pyenv/versions/3.11.6/bin/python3.11
```

6. Finally, you should be able to run `poetry install` to install all dependencies and `poetry shell` to manually spawn your virtual environment.