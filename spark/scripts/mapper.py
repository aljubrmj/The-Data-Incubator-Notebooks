#!/usr/bin/env python3

import sys

def read_input(file, encoding='utf-8'):
    for line in file:
        yield line.decode(encoding)

def write_line(line, encoding='utf-8'):
    sys.stdout.buffer.write((line + '\n').encode(encoding))

def main(separator='\t'):
    data = read_input(sys.stdin.buffer)
    for line in data:
        for word in line.split():
            write_line('%s%s%d' % (word, separator, 1))

if __name__ == "__main__":
    main()
