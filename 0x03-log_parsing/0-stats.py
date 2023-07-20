#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""

import sys
import re

def process_log_entry(log_entry):
    """ Regular expression to extract data from log entry"""
    log_pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\] "GET \/projects\/260 HTTP\/1\.1" (\d+) (\d+)'
    match = re.match(log_pattern, log_entry)

    if match:
        ip_address = match.group(1)
        timestamp = match.group(2)
        status_code = match.group(3)
        file_size = int(match.group(4))
        return ip_address, timestamp, status_code, file_size
    return None

def print_stats(total_file_size, status_code_counts):
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print(f"{status_code}: {count}")

""" Initialize variables to store metrics"""
total_file_size = 0
status_code_counts = {}

try:
    line_count = 0

    for line in sys.stdin:
        log_entry = line.strip()

        """ Process log entry and extract relevant data"""
        data = process_log_entry(log_entry)
        if data:
            ip_address, timestamp, status_code, file_size = data

            """ Update metrics"""
            total_file_size += file_size
            status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

            """ Print statistics after every 10 lines """
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_counts)
                print()

except KeyboardInterrupt:
    """If a keyboard interruption (CTRL + C) occurs, 
    print final statistics"""
    print_stats(total_file_size, status_code_counts)