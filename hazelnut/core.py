#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class MemInfo(object):

    def __init__(self, path='/proc/meminfo'):
        self.path = path

    def fileobj(self):
        return open(self.path, 'r')

    def __str__(self):
        with self.fileobj() as f:
            lines = [line.strip() for line in f]
        return '\n'.join(lines)

    def __repr__(self):
        return self.__str__()

    def dict(self):
        with self.fileobj() as f:
            d = dict(x.strip().split(None, 1) for x in f)
            d = {key.strip(':'): item.strip() for key, item in d.items()}
        return d

    def search(self, regex):
        with self.fileobj() as f:
            matcher = re.compile(regex, re.IGNORECASE)
            return [k for k in f if matcher.match(k)]

    def get(self, string):
        with self.fileobj() as f:
            for item in f:
                line = item.strip()
                if line.startswith(string):
                    match = re.findall(r'([0-9]+)\s', line)
                    return int(match[0])
