<!-- Package for performing string operations -->

Step 1: Create a package directory

    Create a new directory inside the project directory for your package
        ```mkdir ft_package```
Step 2: Create module files
    ft_string_operations.py
    count_in_list.py

Step 3: Create a pyproject.toml file
    specify the necessary details

Setp 4: Run command
        ```flit build```

Step 5:
    ``` • pip install ./dist/ft_package-0.0.1.tar.gz
        • pip install ./dist/ft_package-0.0.1-py3-none-any.whl```

Step 6: Use the package
    In your Python code, import the package

To display a list of installed packages along with their versions.
    ```pip list```

To display detailed information about the specified package, including metadata such as version,
location, dependencies, and more.
    ```pip show -v ft_package```

Alternatively...

Step 3: Create a setup.py file

    Create a file in the project directory called "setup.py" to define the package metadata:
        from setuptools import setup, find_packages

Step 4: Build the package

    Build the package using the following command in the terminal:
        ```python setup.py sdist bdist_wheel```
    This command will create both source distribution and wheel distribution files in the dist directory.

Step 5: Install the package
    Install the package using pip:
        ```pip install .```
    This installs the package in your Python environment.

Step 6: Use the package
    In your Python code, import the package

To display a list of installed packages along with their versions.
    ```pip list```

To display detailed information about the specified package, including metadata such as version,
location, dependencies, and more.
    ```pip show -v ft_package```
    
To upload your Python package distribution files to the Python Package Index (PyPI) using the twine tool. 
    ```twine upload dist/*```


Ref: https://www.turing.com/kb/how-to-create-pypi-packages#what-is-pypi?


