# -*- coding: utf-8 -*-

"""Main module."""

import xml.etree.cElementTree as etree

import gzip


def extract_als(fname):
    with gzip.open(fname, 'rb') as f:
        return f.read()


def parse_als(fname):
    file_content = extract_als(fname)
    root = etree.fromstring(file_content)
    return root


