#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='edx-grades-api',
    version='1.0.1',
    description='Grades REST Api for Open edX',
    author='IONISx',
    url='https://github.com/IONISx/edx-grades-api',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests', '*.tests'])
)
