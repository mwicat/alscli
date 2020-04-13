# -*- coding: utf-8 -*-

"""Main module."""

import xml.etree.cElementTree as etree

import gzip


def parse_als(fname):
    with gzip.open(fname, 'rb') as f:
        file_content = f.read()
    root = etree.fromstring(file_content)
    return root


