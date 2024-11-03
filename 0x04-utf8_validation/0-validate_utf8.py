#!/usr/bin/python3
"""
0-validate_utf8.py

This module provides a function to determine if a given data set
represents a valid UTF-8 encoding.

The UTF-8 encoding rules are as follows:
- A UTF-8 character can be 1 to 4 bytes long.
- For a byte sequence to be valid UTF-8:
  - A 1-byte character has the form 0xxxxxxx.
  - A 2-byte character has the form 110xxxxx 10xxxxxx.
  - A 3-byte character has the form 1110xxxx 10xxxxxx 10xxxxxx.
  - A 4-byte character has the form 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx.
  
The function uses bitwise operations to check these patterns and 
ensures that each byte in the sequence adheres to the UTF-8 standard.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (list of int): A list of integers where each integer represents one byte of data.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0  # Number of bytes in the current UTF-8 character
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF  # Only consider the 8 least significant bits

        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0

