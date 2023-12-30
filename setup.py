"""
Copyright (C) 2023 Austin Choi
See end of file for extended copyright information
"""

from setuptools import setup, find_packages

setup(
    name='chpm',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'chpm = chpm.main:main'
        ],
    },
)

"""
Copyright (C) 2023 Austin Choi

Choice Project Manager
A project template manager created using Jinja2 in python to create new project and add new files to projects created with this
This code is licensed under the GNU General Public License 3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
