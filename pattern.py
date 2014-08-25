#!/usr/bin/env python3
from itertools import islice
from collections import deque

def char_range(start, end):
    """
    Generates all characters in the range, inclusive.
    """
    for c in range(ord(start), ord(end)+1):
        yield chr(c)

def generate_pattern():
    for begin in char_range('A', 'Z'):
        for mid in char_range('a', 'z'):
            for i in range(1, 10):
                yield begin
                yield mid
                yield str(i)

def adress_to_pattern(adress, big_endian=False):
    if adress.startswith('0x'):
        adress = adress[2:]

    adress = [adress[i:i+2] for i in range(0, 8, 2)]

    pattern = [chr(int(x, 16)) for x in adress]

    if not big_endian:
        pattern = pattern[::-1]

    return pattern

def find_offset(pattern):
    sequence = generate_pattern()
    window = deque(maxlen=4)
    offset = 0
    pattern = list(pattern)

    for i in range(window.maxlen):
        window.append(next(sequence))

    while list(window) != pattern:
        offset += 1
        window.append(next(sequence))

    return offset


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Create some pattern to match buffer overflows.')
    parser.add_argument('--generate', '-g', metavar='LEN', type=int, help='Generate a pattern of given length.')
    parser.add_argument('--match', '-m', metavar='PATTERN', help='Match the given pattern')
    args = parser.parse_args()

    if args.generate:
        # Prints the correct pattern and exits
        pattern = "".join(islice(generate_pattern(), args.generate))
        print(pattern)

    if args.match:
        pattern = adress_to_pattern(args.match)
        offset = find_offset(pattern)
        print("Found matching pattern at offset {offset}".format(offset=offset))



if __name__ == "__main__":
    main()
