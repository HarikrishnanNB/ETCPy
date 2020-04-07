#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains helper functions for reading and writing files.

@author: Pranay S. Yadav
"""

# Import functions from standard library modules
from pathlib import Path
from csv import DictWriter

def read(filepath, recode=True, delimiter=None):
    if not isinstance(filepath, Path):
        filepath = Path(filepath)
    text = filepath.read_text()

    if delimiter:
        text = ''.join(text.split(delimiter))

    if recode:
        alphabets = sorted(set(text))
        replacer = dict((y,str(x+1)) for x,y in enumerate(alphabets))
        for key in replacer:
            text = text.replace(key, replacer[key])

    return tuple(map(int, text))

def save(out, filename):

    with open(filename, 'w') as fileout:
        writer = DictWriter(fileout, fieldnames=out[0].keys(), delimiter=',')
        writer.writeheader()
        writer.writerows(out)
        print(f">> Data successfully stored to disk as {filename}")