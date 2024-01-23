# from setuptools import setup, find_packages

# setup(
#     name='ft_package',
#     version='0.0.1',
#     author='nali',
#     author_email='nali@student.42.ae',
#     description='String Operations',
#     packages=find_packages(),
#     classifiers=[
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
# )

import sys

try:
    from setuptools import setup
except ImportError:
    sys.exit("setuptools is required.")

setup()

"""
This setup.py file is minimal because flit(A Python packaging tool designed to simplify the process of
distributing Python projects.) relies on the information specified in the pyproject.toml file. 
The setup() call in this script will automatically read metadata and configuration from pyproject.toml.
"""
