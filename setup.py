import io
import os
import sys
import setuptools
from setuptools import find_packages, setup, Command

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'PDFCracker',
  packages = ['PDFCracker'],
  version = '0.1',
  license='MIT',
  description = "Crack PDF password is easy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Hebert Cisco',
  author_email = 'hebertcisco@outlook.com',
  url = 'https://github.com/hebertcisco/PDFCracker',
  py_modules=['mypackage'],
  entry_points={'console_scripts': ['mycli=mymodule:cli'],},
  keywords = ['PDF', 'PDFCracker', 'YET CRYPTIC'],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.4',  
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6'
  ],
  python_requires='>=3.1',
)