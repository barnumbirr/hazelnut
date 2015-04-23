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
            match = filter(matcher.match, f)
        return match

    # This is a WIP, does not work for the time beeing.
    def get(self, string):
        # TODO:
        # match input string
        # regex is still wonky, needs fixing
        with self.fileobj() as f:
            for line in f:
                match = re.findall(r'\d+', line)
            return match
