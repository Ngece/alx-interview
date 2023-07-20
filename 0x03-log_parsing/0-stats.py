#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""

import sys

""" Initialize a dictionary to count status codes occurrences """
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}

""" Initialize variables to store metrics """
file_size = 0
counter = 0

try:
    """ Read log entries from stdin line by line """
    for line in sys.stdin:
        counter += 1

        """ Split the log entry into individual elements """
        data = line.split()
        
        """ Check if the log entry has the required format with 
        enough elements """
        if len(data) > 2:
            """ Extract the file size from the log entry and add it 
            to the total """
            file_size += int(data[-1])
            
            """ Extract the status code from the log entry and update its 
            count in the dictionary """
            if data[-2] in status_codes:
                status_codes[data[-2]] += 1

        """ Print statistics after every 10 lines """
        if counter == 10:
            print("File size: {}".format(file_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
            counter = 0

except KeyboardInterrupt:
    """ If a keyboard interruption (CTRL + C) occurs, 
    print final statistics """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
    raise

""" Print final statistics when the end of stdin is reached """
print("File size: {}".format(file_size))
for key, value in sorted(status_codes.items()):
    if value != 0:
        print("{}: {}".format(key, value))
