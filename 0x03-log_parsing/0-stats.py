#!/usr/bin/python3
"""
Log Parsing Script
Reads stdin line by line, parses logs, and outputs metrics.
"""

import sys

# Initialize metrics
total_size = 0
status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}


def print_metrics():
    """Print the accumulated metrics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Read input line by line
line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
        line_count += 1
        try:
            # Split the line and extract required fields
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract file size and status code
            file_size = int(parts[-1])
            status_code = parts[-2]

            # Update metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
        except (ValueError, IndexError):
            # Skip invalid lines
            continue

        # Print metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle Ctrl+C
    print_metrics()
    raise

# Print final metrics
print_metrics()
