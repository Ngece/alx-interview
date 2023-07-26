#!/usr/bin/env python3
""" UTF-8 Validation """

import codecs

def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    try:
        if isinstance(data, bytes):
            data.decode()
        else:
            return False
    except UnicodeDecodeError:
        return False
    return True