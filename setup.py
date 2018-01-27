#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017-2018 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import codecs
import os
import re

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))


# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    try:
        f = codecs.open(os.path.join(here, *file_paths), 'r', 'latin1')
        version_file = f.read()
        f.close()
    except:
        raise RuntimeError("Unable to find version string.")

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
try:
    f = codecs.open('README.rst', encoding='utf-8')
    long_description = f.read()
    f.close()
except:
    long_description = ''

try:
    f = codecs.open('requirements.txt', encoding='utf-8')
    requirements = f.read().splitlines()
    f.close()
except:
    requirements = []


setup(
    name='ansible_template_ui',
    version=find_version('ansible_template_ui/__init__.py'),
    description='Web UI for testing ansible templates',
    long_description=long_description,
    keywords='ansible jinja jinja2 template ansible-template-ui',
    author='Matt Martz',
    author_email='matt@sivel.net',
    url='https://github.com/sivel/ansible-template-ui',
    license='Apache License, Version 2.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=requirements,
    package_data={
        '': [
            'client/*',
        ]
    },
)
