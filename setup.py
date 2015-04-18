#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='hazelnut',
    version='0.3',
    url='https://github.com/c0ding/hazelnut',
    download_url='https://github.com/c0ding/hazelnut/archive/master.zip',
    author='Martin Simon',
    author_email='me@martinsimon.me',
    license='Apache v2.0 License',
    packages=['hazelnut'],
    description='A pythonic library to parse /proc/meminfo',
    long_description=file('README.md','r').read(),
    keywords=['memory', 'RAM', 'system information', 'meminfo', '/proc'],
)
