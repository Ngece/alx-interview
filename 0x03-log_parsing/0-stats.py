#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0

try:
    for line in sys.stdin:
        counter += 1
        data = line.split()
        if len(data) > 2:
            file_size += int(data[-1])
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1
        if counter == 10:
            print("File size: {}".format(file_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
    raise
print("File size: {}".format(file_size))
for key, value in sorted(status_codes.items()):
    if value != 0:
        print("{}: {}".format(key, value))
