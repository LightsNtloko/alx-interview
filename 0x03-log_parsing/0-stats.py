#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def signal_handler(sig, frame):
    """Handle keyboard interrupt and print statistics."""
    print_stats()
    sys.exit(0)

def print_stats():
    """Print the collected statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Process stdin line by line
for line in sys.stdin:
    line_count += 1

    # Parse the line
    parts = line.split()
    if len(parts) < 7:
        continue

    # Extract relevant parts
    try:
        ip = parts[0]
        date = parts[2][1:]  # Remove the leading '['
        method = parts[5][1:]  # Remove the leading '"'
        status_code = int(parts[6])
        file_size = int(parts[7])
    except (IndexError, ValueError):
        continue

    # Check if the method is GET and if status code is valid
    if method == "GET" and status_code in status_codes:
        total_size += file_size
        status_codes[status_code] += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Final statistics on exit
print_stats()
