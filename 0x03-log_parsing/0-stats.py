#!/usr/bin/python3
"""
Log parsing script to compute metrics from logs.
"""
import sys

def print_metrics(total_size, status_counts):
    """
    Prints the current metrics: total file size and status code counts.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary of status codes and their counts.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def main():
    """
    Main function to parse logs and compute metrics in real-time.
    """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                # Parse the log line
                parts = line.split()
                if len(parts) < 7:
                    continue

                file_size = int(parts[-1])
                status_code = int(parts[-2])

                # Update metrics
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            except (ValueError, IndexError):
                # Ignore malformed lines
                continue

            # Print metrics after every 10 lines
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_metrics(total_size, status_counts)
        raise

    # Final metrics printout
    print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
