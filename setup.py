#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.7',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(carlba): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='dot_sync',
    version='0.1.0',
    description="A tool for syncing dotfiles between linux machines",
    long_description=readme + '\n\n' + history,
    author="Carl Bäckström",
    author_email='genzorg@gmail.com',
    url='https://github.com/carlba/dot_sync',
    packages=find_packages(include=['dot_sync']),
    entry_points={
        'console_scripts': [
            'dot_sync=dot_sync.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='dot_sync',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
