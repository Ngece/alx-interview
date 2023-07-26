#!/usr/bin/env python3
""" UTF-8 Validation """

import codecs

def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    try:
        codecs.getdecoder("utf-8")(data)
        return True
    except UnicodeDecodeError:
        return False