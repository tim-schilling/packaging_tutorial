# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys
from setuptools import Extension, find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()

compile_extensions = (
    # Python 3+
    sys.version_info >= (3,)
    # Not Jython
    and not sys.platform.startswith("java")
    # Not PyPy
    and "__pypy__" not in sys.builtin_module_names
    # Not explicitly disabled
    and (os.environ.get("BUILD_DISABLE_EXTENSIONS", "") == "")
)
if compile_extensions:
    ext_modules = [
        Extension(
            name=str("example_package._example_c"),
            sources=[str("src/example_package/_example_c.c")],
            optional=True,
        )
    ]
else:
    ext_modules = []

setup(
    name="packaging-tutorial-tim-schilling",
    version="0.0.2",
    author="Tim Schilling",
    author_email="schillingt@better-simple.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tim-schilling/packaging_tutorial",
    project_urls={
        "Bug Tracker": "https://github.com/tim-schilling/packaging_tutorial/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    ext_modules=ext_modules,
    packages=find_packages(where="src"),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
)
