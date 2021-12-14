#!/usr/bin/env python
from os.path import exists

from setuptools import setup

import versioneer

setup(
    name="aemcmc",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Miscellaneous MCMC samplers written in Aesara",
    url="http://github.com/aesara-devs/aemcmc",
    maintainer="Brandon T. Willard",
    maintainer_email="aesara-devs@gmail.com",
    packages=["aemcmc"],
    install_requires=[
        "numpy>=1.18.1",
        "scipy>=1.4.0",
        "aesara",
        "aeppl",
    ],
    tests_require=["pytest"],
    long_description=open("README.md").read() if exists("README.md") else "",
    long_description_content_type="text/markdown",
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
