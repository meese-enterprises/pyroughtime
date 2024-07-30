#!/usr/bin/env python3

import os
from setuptools import setup

# Get key package details from pyroughtime/__version__.py
about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "pyroughtime", "__version__.py")) as f:
    exec(f.read(), about)

# Load the README file and use it as the long_description for PyPI
with open("README.md", "r") as f:
    readme = f.read()

# Package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
setup(
  name=about["__title__"],
  description=about["__description__"],
  long_description=readme,
  long_description_content_type="text/markdown",
  version=about["__version__"],
  author=about["__author__"],
  author_email=about["__author_email__"],
  url=about["__url__"],
  packages=["pyroughtime"],
  include_package_data=True,
  # Can't build ed25519 on Python 3.12 yet
  python_requires=">=3.7.*,<=3.11.*",
  install_requires=["ed25519", "pycrypto"],
  license=about["__license__"],
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.7",
  ],
  keywords="roughtime, time, timestamp, security, cryptography",
)
