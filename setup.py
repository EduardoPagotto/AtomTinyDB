#!/usr/bin/env python3
'''
Created on 20200323
Update on 20200627
@author: Eduardo Pagotto
 '''

import setuptools

PACKAGE = "AtomTinyDB"
VERSION = __import__(PACKAGE).__version__

setuptools.setup(
    name="AtomTinyDB",
    version=VERSION,
    author="Eduardo Pagotto",
    author_email="edupagotto@gmail.com",
    description="TinyDB atomico to multi-thread updates",
    long_description="TinyDB atomico to multi-thread updates",
    long_description_content_type="text/markdown",
    url="https://github.com/EduardoPagotto/AtomTinyDB.git",
    packages=setuptools.find_packages(),
    #packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    install_requires=['tinydb']
)
